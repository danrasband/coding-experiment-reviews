# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    integers = range(0,x)
    multiples_3 = [x for x in integers if x%3 == 0]
    # print(multiples_3)
    multiples_5 = [x for x in integers if x%5 == 0]
    # print(multiples_5)
    to_remove = [x for x in multiples_3 if x in multiples_5]
    print(to_remove)
    # print(type(to_remove))
    multiples_3.extend(multiples_5)
    # print(master)
    # print(type(master))
    if to_remove is None:
        output = multiples_3
    else:
        for x in range(len(multiples_3)):
            print(x)
            if multiples_3[x] in to_remove:
                multiples_3.pop(x)

    return output
