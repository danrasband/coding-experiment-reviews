# Feedback

## 1. Count of Largest Integer

This is concise, clear, and appropriate. Nice work! There is a more performant
way of computing this value, which you can see in the

## 2. Reverse Digits

There are a couple of methods and facts that could help you simplify your
response. The first is that casting a string to an integer works even if there
are zeros at the front, so you don't really need to account for that
separately, as long as you remove any negative sign first. Secondly, instead
of checking the string for a negative sign, it's probably easier to check the
integer first to see if it's negative, which will make the rest of your code
simpler.

See [this solution](https://github.com/danrasband/coding-experiment-reviews/blob/master/golden/python/reverse_digits.py) for an example.

## 3. Maximum Product

Nice start on this one! It's excellent that you checked for the exceptional
cases right away. Given more time, I think you would have gotten it without a
problem.
