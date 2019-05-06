# Feedback

## 1. Count of Largest Integer

Great job. I'm not sure what `max_apps` stands for. Sometimes it pays to use
the full word in a variable name. This solution misses the edge case where `A`
is empty.

## 2. Sum of Certain Multiples

Nice work! While it makes for a bit of a long line, you could alternatively
have written the following in your check:

```python
if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
```

This would have made your solution just a tad bit more concise.

## 3. Find Maximum Product

Nice job getting to the third problem! And good job checking for the edge cases
straight from the get-go. I'm a bit believer in the idea of return clauses.
Basically, you could have done without the `else` because you returned in the
first `if` clause, i.e.

```python
if len(B) == 0 or X > len(B):
    return 0
else:
    product = 0
    # ...
```

Could have been this:

```python
if len(B) == 0 or X > len(B):
   return 0

product = 0
# ...
```

This reduces unnecessary indentation and makes it easier to read your code.

Another thing to note is that you could have returned early in the
`len(B) == 1` case.

Overall, great work! I love that you used `reduce`.
