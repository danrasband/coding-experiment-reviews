# Feedback

## 1. Sum of Integers in a String

Nice job using the radix parameter in the `parseInt` function! A lot of people
miss that. I also like your use of `reduce` and a constant function. This is
fun ES6 code. You might want to also look at the `map` method for translating
elements of an array. One last thing: you needed to account for the empty
string scenario. All-in-all great work.

## 2. Sum of Certain Multiples

I like your approach to making sure the number isn't a multiple of both 3 and
5. In your `for (let i = 1; i < x; i++)` statement, you could have gone the
extra mile and started at `i = 3`, but I don't think I even thought to do that
in my "golden" solution. Overall great work!

## 3. Longest Common Prefix

I like this approach of sorting by length first. It's arguably not the most
performant, but it works. Another method is to simply go through the array
once, assuming the first element of the array is the longest common prefix,
and adjusting that assumption as you go.
