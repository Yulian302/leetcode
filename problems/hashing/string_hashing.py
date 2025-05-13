

def hash_string(string):
    curr_hash = 0
    p = 31
    MOD = 1e9+9
    power = 1  # tracks p^i % MOD
    for i in range(len(string)):
        curr_hash = (curr_hash + ord(string[i]) * power) % MOD
        power = (power * p) % MOD

    return curr_hash
# hash = s[0]*p^0 + s[1]*p^1 + s[2]*p^2 + .. + s[n-1]*p^(n-1)


def group_identical_strings(strings):
    hashes = []
    for i, string in enumerate(strings):  # O(nm)
        hashes.append((hash_string(string), i))
    hashes.sort()  # nlogn

    prev_hash = None
    curr_group = []
    groups = []
    for h, idx in hashes:
        if h == prev_hash:
            curr_group.append(idx)
        else:
            if curr_group:
                groups.append(curr_group)
            prev_hash = h
            curr_group = [idx]

    if curr_group:
        groups.append(curr_group)

    res = []
    for group in groups:
        group_strings = [strings[i] for i in group]
        res.append(group_strings)
    return res


def group_identical_strings_better(strings):
    hash_map = {}
    for string in strings:
        hashed_string = hash_string(string)
        if hashed_string not in hash_map:
            hash_map[hashed_string] = []
        hash_map[hashed_string].append(string)

    groups = [group for group in hash_map.values()]
    return groups


def count_unique_substrings(string):
    count = 0
    n = len(string)
    for l in range(1, n+1):  # [1,n]
        hash_set = set()
        for i in range(n-l+1):  # [0, n-l]
            hash_set.add(hash_string(string[i:i+l]))
        count += len(hash_set)
    return count


print(group_identical_strings(["hello", "my", "name", "hello"]))
print(group_identical_strings_better(["hello", "my", "name", "hello"]))
print(count_unique_substrings("hello"))
