import queue
import time
import threading
from os import path


class TrieNode:
    def __init__(self, ch=""):
        self.ch = ch
        self.children = {}
        self.is_end_of_word = False


def create_trie(filename: str):
    if not filename:
        return
    with open(file=filename, mode='r', encoding='utf-8') as file:
        root = TrieNode()
        for line in file:
            word = line.split('\n')[0]
            if not word:
                continue
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode(c)
                curr = curr.children[c]
            curr.is_end_of_word = True
    return root


def autocomplete(root: TrieNode, term: str) -> list:
    if not term:
        return []

    ans = []

    def dfs(node: TrieNode, path: list):
        if node.is_end_of_word:
            ans.append("".join(path))

        for ch in node.children.keys():
            dfs(node.children[ch], path+[ch])

    curr = root
    for c in term:
        if not curr.children[c]:
            return []
        curr = curr.children[c]

    dfs(curr, list(term))
    return ans


def read_kbd_input(inputQueue):
    while (True):
        input_str = input()
        inputQueue.put(input_str)


def autocomplete_cli(trie):
    EXIT_COMMAND = "exit"

    print("Start typing (Enter 'exit' to exit):")

    input_queue = queue.Queue()
    input_thread = threading.Thread(
        target=read_kbd_input, args=(input_queue,), daemon=True)
    input_thread.start()

    while True:
        if input_queue.qsize() > 0:
            input_str = input_queue.get()

            if (input_str == EXIT_COMMAND):
                print("Exiting...")
                break
            suggestions = autocomplete(trie, input_str)
            print(suggestions)
        time.sleep(0.01)


if __name__ == "__main__":
    trie = create_trie(path.abspath(
        path.join(path.dirname(__file__), 'words.txt')))
    autocomplete_cli(trie)
