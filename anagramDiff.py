from collections import defaultdict

def anagram_diff(start, end):
    if len(start) == 0 or len(start) != len(end):
        raise Exception("invalid input")
    letter_count = defaultdict(lambda: 0)

    for i in range(len(start)):
        letter_count[start[i]] += 1
        letter_count[end[i]] -= 1

    return_val = 0
    for i in letter_count:
        if letter_count[i] > 0:
            return_val += letter_count[i]

    print start, end, return_val

    return return_val


assert(anagram_diff("abba", "bbaa") == 0)
assert(anagram_diff("bond", "down") == 1)
assert(anagram_diff("xxxx", "yyyy") == 4)
assert(anagram_diff("xxyy", "xxxx") == 2)
