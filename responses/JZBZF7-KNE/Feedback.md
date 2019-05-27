# Feedback

## 1. Count of Largest Integer

Nice job checking for the empty array scenario. It would have been a tiny bit
more concise to do it this way:

```python
if len(A) == 0:
    return 0
```

Or even this, since the empty array resolves as false:

```python
if not A:
    return 0
```

## 2. Sum of Certain Multiples

I like your approach. A faster way to get where you were going is with the
`range()` function, using three arguments.

## 3. Find Maximum Product

It looks like you ran out of time on this one. Nice attempt!
