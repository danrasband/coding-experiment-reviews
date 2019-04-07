def solution(A):
    index = 0
    result = ""
    while True:
        currentChar = "!"
        for word in A:
            if len(word) <= index:
                return result
            if currentChar == "!":
                currentChar = word[index]
                continue
            if currentChar != word[index]:
                return result
        result += currentChar
        index += 1
    return result
