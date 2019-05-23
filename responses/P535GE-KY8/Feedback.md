# Feedback

## 1. Sum of Integers in a String

Great solution! Note that you don't need to use `+=`, since the value yielded
at the end of the block is passed on to the next iteration automatically.

## 2. Reverse Digits

Excellent choice to store the sign ahead of time. I also like that your
solution doesn't use strings to do the reversal. Very cool.

## 3. Longest Common Prefix

I like this solution quite a bit. I wasn't familiar with `Enumerable#drop`,
but it works quite nicely in this scenario (and its use would improve our
"golden" solution). The guard clause and the break are good choices to do as
little work as possible.

See the "golden" solution for another approach to tackling the problem,
specifically the edge case checking at the beginning of the method.
