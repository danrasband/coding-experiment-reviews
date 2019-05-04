def solution(words):
    if words == []:
        return ''

    if len(words) == 1:
        return words[0]

    prefix = words[0]
    for word in words:
        new_prefix = ''
        for i in range(min(len(prefix), len(word))):
            if prefix[i] != word[i]:
                break
            new_prefix += word[i]
        prefix = new_prefix

    return prefix
