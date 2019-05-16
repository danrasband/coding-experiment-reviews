# Feedback

## 1. Count of Largest Integer

This is an approach I would have definitely taken in the past. It's elegant,
and works well. There's a more memory-performant method that requires you keep
track of the largest integer and its count, resetting the count to 1 every time
you come upon a larger integer.

## 2. Sum of Certain Multiples

I'm not a huge fan of the variables `ele` and `res`. I'd prefer the full words.
Nice job checking for `ele % 15 != 0`. Because of how Python short-circuits
`and` and `or`, it's necessary to use parentheses to get the correct outcomes
when checking for multiples.

## 3. Longest Common Prefix

Nice job checking for the edge cases at the beginning. Your solution is
interesting, but doesn't quite get at the core of the problem. I'm guessing
you just ran out of time.

Overall, nice job working through these!
