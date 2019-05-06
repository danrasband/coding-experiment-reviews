# Feedback

## 1. Sum of Integers in a String

There's no need for a semicolon on line 5 and no need for the word `return` on
line 9. Ruby is forgiving, though.

I like how this only goes through the list once. It requires more lines of code
to do it this way, but it's more performant, which is awesome.

## 2. Reverse Digits

It looks like you gave up on this one.

## 3. Longest Common Prefix

This is a tough one. Good effort! Your solution isn't too performant thanks to
the `a.each` within another `a.each`. A better approach is to simply assume
that your first word is the longest common prefix, then as you work through
the list, adjust the cached prefix, comparing it with one word at a time. What
you end up with in the end is the longest.
