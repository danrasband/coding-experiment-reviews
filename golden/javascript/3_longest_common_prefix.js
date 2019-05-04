function solution(words) {
    if (!words.length) {
        return '';
    }
    if (words.length == 1) {
        return words[0];
    }

    var prefix = words[0];
    words.forEach((word) => {
        newPrefix = '';
        for (var i = 0; i < Math.min(prefix.length, word.length); i++) {
            if (prefix[i] != word[i]) {
                break;
            }
            newPrefix += word[i];
        }
        prefix = newPrefix;
    });
    return prefix;
}
