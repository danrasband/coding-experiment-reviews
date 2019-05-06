# Feedback

## 1. Sum of Integers in a String

Very nice solution. The only change I would make is to remove the extra
variable assignment (`result = `) and replace that with the return. Oh, and you
should also check for the the case of the empty string.

## 2. Sum of Certain Multiples

This is a perfect solution. Nice touch on skipping 0 through 2 in the loop.

## 3. Longest Common Prefix

This is an interesting approach. I'm not sure I get why you're using the `
currentChar == "!"` stuff. It's possible that the string has a "!" in it,
which could throw off your solution in some cases.

It makes things easier to assume that the first word is in fact the longest
common prefix, and then whittle it down from there.

Lastly, it's a good idea to check for the empty array and single value array
scenarios before digging in.
