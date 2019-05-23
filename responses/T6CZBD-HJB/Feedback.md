# Feedback

## 1. Sum of Integers in a String

I like your approach here. It could have been done quite a bit more simply,
however. Using `int` to cast a string to an integer works even with `+` and `-`
prefixes. In addition, you need to check for the empty string case, in which
casting will not work.

## 2. Sum of Certain Multiples

While this isn't the most performant solution out there, it's very readable and
is a fun way of getting at the right answer. It looks like you didn't quite get
to the point of summing the array, but you were definitely going in the right
direction. A way to make this more performant might be to iterate over the
numbers only once, checking each number along the way as to whether or not it
should be included in the final array. Then all you have to do at the end is
use the Python built-in function `sum()` on the resulting array.

## 3. Find Maximum Product

It looks like you ran out of time. Nice work anyway!
