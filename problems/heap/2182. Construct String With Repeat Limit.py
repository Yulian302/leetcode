# https://leetcode.com/problems/construct-string-with-repeat-limit/
# Difficulty: Medium (Hard)
# Tags: heap min_heap lexicographical

# Problem
# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

# Return the lexicographically largest repeatLimitedString possible.

# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

# Solution
# Time O(nlogn) and space O(k)
# We count frequencies of each character using a freq map. Then we create a max heap based on char ascii code value (to prioritize lexicographically greater values). After that we pop from max heap in a loop and check for chars that remain due to repeat limit. Then more complex logic appears: if we still have items in max heap, we get that item, append to string one time and then push it back to max heap. Then we push our remaining item that we found before to heap once again. This logic preserves priority for lexicographically larger resulting string.

import heapq
from typing import Counter


def repeatLimitedString(s: str, repeatLimit: int) -> str:
    counter = Counter(s)
    # dict: [char: freq]
    max_heap = []
    for ch, freq in counter.items():
        heapq.heappush(max_heap, (-ord(ch), freq))

    ans = []

    while max_heap:
        code, freq = heapq.heappop(max_heap)
        ch = chr(-code)
        max_freq = min(freq, repeatLimit)

        ans.append(ch * max_freq)
        freq -= max_freq

        if freq > 0:
            if max_heap:
                next_code, next_freq = heapq.heappop(max_heap)
                next_ch = chr(-next_code)

                ans.append(next_ch)

                if next_freq > 1:
                    heapq.heappush(max_heap, (next_code, next_freq - 1))

                heapq.heappush(max_heap, (code, freq))
            else:
                break
    return "".join(ans)
