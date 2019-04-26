# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    solution = ""
    prefix_dict = dict()
    
    for element in A:
        first_letter = element[0]
        if first_letter not in prefix_dict.keys():
            prefix_dict[first_letter] = 1
        else:
            prefix_dict[first_letter] += 1
            
    top_letter = str(sorted(prefix_dict, key=prefix_dict.get, reverse=True)[0])
    
    filtered_A = list(filter(i for i in A if i[0] == top_letter))
    