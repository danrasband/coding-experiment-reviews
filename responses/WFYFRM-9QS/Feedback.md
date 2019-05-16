# Feedback

## 1. Count of Largest Integer

It looks like you were going for some different approaches here with the
unused `cntDict`. It would have been a little cleaner to use a guard clause at the beginning of the function body, rather than to wrap most of the code in a big `if/else` clause:

```python
if not A:
    return 0

maxNum = A[0]
# ...
```

All in all, this is a very appropriate and performant approach. Nice!

## 2. Sum of Certain Multiples

Interesting choice to specifically check for 4 and 5. It looks like I may
have briefly misled you with the (admittedly poorly-worded) instructions. The
answer for 5 is actually 8, since both 3 and 5 count. Otherwise, I really like
this set-based approach.

## 3. Longest Common Prefix

It looks like you ran out of time. Nice hustle!
