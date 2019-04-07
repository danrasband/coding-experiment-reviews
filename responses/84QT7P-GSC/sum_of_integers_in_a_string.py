# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    sum = 0
    num_list = S.split(",")
    for i in range(0, len(num_list)):
        sum += int(num_list[i])
    #print(sum)
    return sum
