# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    # write your code in Python
    K = len(B)

    if K == 0 or X > K:
        return 0
    else:
        result = 0
        start = 0
        end = X
        runs = K = X
        print(f'runs = {runs}')
        for runs in range(1,K - X):
            run_result = 1
            for x in B[start:end]: 
                run_result = run_result * x
            if run_result > result:
                result = run_result
            start = start + 1
            end = end + 1
        print(result)
        return result