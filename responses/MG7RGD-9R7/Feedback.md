# Feedback

## 1. Count of Largest Integer

Very nice approach. Seeding the process with the first element is perfect. The
code is easy to follow and pretty concise. One possible improvement is to skip
the first `if` statement:

```python
if A[i+1] == maxnum:
    maxcount+=1
elif A[i+1] > maxnum:
    maxnum = A[i+1]
    maxcount = 1
# No need to check the less than case, since it will continue by default.
```

## 2. Sum of Certain Multiples

This is an interesting solution, and I like the idea behind it. You could get to where you were going a little easier, I think, with the `range()` function using three arguments. As it is, it's a bit on the harder side to follow.

## 3. Longest Common Prefix

You were on the right track here. It looks like you just ran out of time. Nice
attempt!
