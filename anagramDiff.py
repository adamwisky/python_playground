def anagram_diff(start, end):
    if len(start) == 0 or len(start) != len(end):
        raise Exception("invalid input")
    letter_count = [0] * 26

    for i in range(len(start)):
        start_char_val = ord(start[i]) - ord('a')
        if(start_char_val < 0 or start_char_val > 25):
            raise Exception("invalid input")
        letter_count[start_char_val] += 1

        end_char_val = ord(end[i]) - ord('a')
        if(end_char_val < 0 or end_char_val > 25):
            raise Exception("invalid input")
        letter_count[end_char_val] -= 1

    return_val = 0
    for i in letter_count:
        if i > 0:
            return_val += i

    print start, end, return_val

    return return_val


assert(anagram_diff("abba", "bbaa") == 0)
assert(anagram_diff("bond", "down") == 1)
assert(anagram_diff("xxxx", "yyyy") == 4)
assert(anagram_diff("xxyy", "xxxx") == 2)
