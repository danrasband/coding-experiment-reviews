# Feedback

## 1. Sum of Integers in a String

Great job. Two things to consider: 1) You should check for the empty string
scenario since `''.split('')` returns `['']`, and `''` doesn't convert to an
int very well; and 2) you don't need to check for the `+` in a string, since
casting a string with a plus in it to an integer works great. For example,
`int('+5')` converts the string to `5` with no problems.

## 2. Sum of Certain Multiples

This is an interesting solution. It feels a bit overcomplicated and hard to
follow. I do like the idea of calculating the sum based on the result of
dividing `x` by `3` and `5`, but the resultant solution requires two
additional loops (albeit probably shorter ones than some other solutions), and
makes it harder to catch the multiples of both 3 and 5.

## 3. Find Maximum Product

Since you're using guard clauses in lines 7-10, you don't need the `else` in
line 11. Nice job checking for the edge cases early, though. I like this
solution, though. It's easy to read and grok, and it seems to get the job done.
You may not need to use two separate loops for calculating the largest product,
but the method works, and in the time limit you had, it's great. Nice job!
