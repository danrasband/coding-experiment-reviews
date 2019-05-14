# Feedback

## 1. Count of Largest Integer

Nice job here. A note on style: it's good to separate operators from values and variables with spaces:

```javascript
// Not as readable:
for (i=1; i<A.length; i++) {

// Better:
for (var i = 1; i < A.length; i++) {
```

Your solution has complexity of O(n), which I believe is the best you can get,
so great job!

## 2. Reverse Digits

Nice attempt here. One scenario that you missed is that of negative integers
(e.g. `-500`). I really like your solution to reversing the digits, even if it
isn't the absolute most performant. Last of all, you should always use the
[radix parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt#Parameters)
when using the `parseInt` function to prevent surprises when converting
numbers of different bases.

## 3. Find Maximum Product

Your code looks pretty good (you're missing some `var`s and such), but it
misses the point. I'm guessing you just ran out of time here. Nice try!
