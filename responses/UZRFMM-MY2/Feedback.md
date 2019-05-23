# Feedback

## 1. Count of Largest Integer

This is an elegant solution, just missing the check for an empty array.

## 2. Sum of Certain Multiples

I'm not a big fan of the `count` variable name (what are you counting?), but
the solution is pretty solid. One thing your solution is missing is the check
for when the number (`count` in your case) is a multiple of _both_ 3 and 5 (
i.e. 15), and not add that number to the sum. Otherwise great solution.

## 3. Find Maximum Product

Nice job checking for edge case scenarios upfront. I believe you must have
simply run out of time on this one, but you were definitely going in the right
direction. Nice attempt! One thing to be careful of is starting with 0 as your
max. It's very possible that the true maximum is negative, which would make
your solution fail.
