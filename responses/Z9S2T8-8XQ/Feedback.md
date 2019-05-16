# Feedback

## 1. Sum of Integers in a String

Your code is simple and straightforward. Nice job! A couple of things to note:

1. You should always use the radix operator when using the `parseInt` function to avoid surprises.
2. You should use semi-colons for maximum clarity and good style.
3. You need to account for the empty string case.
4. I personally like the style that includes a space after control words like
`if`, `else`, etc.

## 2. Reverse Digits

Nice job checking for the integer's sign before converting it to a string. One thing that I would recommend is using the ternary operator: `?:`:

```javascript
return isPositive ? parsed : -parsed;
```

## 3. Find Maximum Product

It looks like you may have run out of time on this one. Good try, though!
