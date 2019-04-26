# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    letter_groups, longest_pre = zip(*A), ""

    for letter_group in letter_groups:
        if len(set(letter_group)) > 1: break
        longest_pre += letter_group[0]
    return longest_pre
    
    # I've copy-pasted this task because I don't know how to solve this in 5 min.