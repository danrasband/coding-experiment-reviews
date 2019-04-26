# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    splits = list()
    result = list()
    if len(B) < X:
        return 0
    elif len(B) == 0:
        return 0
    else:
        for i in range(len(B) - X + 1):
            splits.append(B[i:i+X])
        for split in splits:
            result.append(sum(split))
    
        return(max(result))