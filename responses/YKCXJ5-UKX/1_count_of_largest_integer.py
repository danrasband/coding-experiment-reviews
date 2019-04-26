# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    nums = S.split(",")
    
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])
        
    sum_nums = sum(nums)
    
    return sum_nums
