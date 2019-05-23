# Feedback

## 1. Count of Largest Integer

Your solution is very good. It's performant, uses pretty good variable names,
etc. I'm not a fan of the style. Using proper spacing between `if` and
parentheses and surrounding operators can make your code much more legible.
I'd recommend trying out a JavaScript linter like eslint to help improve your
coding style. Two additional notes on your solution: you didn't check for the
empty array case, and you really don't need the whole `if/else` statement at
the end. You can just return `count`, since it will never be less than 0.

## 2. Reverse Digits

This is a good method to solve the problem. When using `parseInt`, it's best
practice to always use the `radix` parameter (e.g. `parseInt(solution, 10)`) to
prevent surprises. Since `tmp` is an integer, you don't need to do `0-tmp` on
line 13; you can simply use `-tmp`.

## 3. Longest Common Prefix

Nice approach here. I like how you thought to reduce the problem to the
shortest string first.

What does `cc` stand for?

You could find the longest common prefix with only two loops instead of the
three you have. Check the "golden" solution for an example.
