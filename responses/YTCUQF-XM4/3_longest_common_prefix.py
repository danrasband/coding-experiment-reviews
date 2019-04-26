# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    max_num = 0
    k = len(B)
    if k == 0:
        pass
    elif X > k:
        pass
    else:
        for i in range(k-(X-1)):
            sub_list = B[i:i+X]
            prod = sub_list[0]
            for j in sub_list[1:]:
                prod *= j
            if prod > max_num:
                max_num = prod
    return max_num
