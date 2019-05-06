# Feedback

## 1. Sum of Integers in a String

Nice work checking for the empty string case, and for handling that using a
return guard clause. Your code is very concise, easy to read, and it gets the
job done. 👍

## 2. Sum of Certain Multiples

The following clause could have been written a bit more simply, i.e.:

```python
if x % 3 == 0 and x % 5 == 0:
```

could have been written simply:

```python
if x % 15 == 0:
```

This is nit-picky, I know.

In addition, you could have done away with the `sum` by simply adding to a tmp
variable along the way and then returning that. Overall, great work.

## 3. Longest Common Prefix

This is a good attempt. I think it makes it a lot easier if you just assume
that the first word is the longest common prefix across the list. Then you
adjust that belief as you go, shortening as necessary a cached prefix along
the way.
