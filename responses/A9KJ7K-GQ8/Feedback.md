# Feedback

## 1. Sum of Integers in a String

Great solution! I would recommend always specify the radix argument when using
`parseInt` (e.g. `parseInt('010', 10)`) to avoid surprises. I also recommend
always using an initial value for `reduce` for maximum explicitness and
clarity. Lastly, I don't think you need the `parseInt` on the accumulator,
since it's logically always guaranteed to be an integer already.

## 2. Sum of Certain Multiples

Nice work. You missed the edge case where the number is a multiple of both 3
_and_ 5. Otherwise, this is great.

## 3. Longest Common Prefix

Your solution is a bit convoluted, but this is likely due to the lack of time
on this problem. The best solutions assume that the first word in the array is
already the longest common prefix, and then work down from there. It lets you
go through the list just once, and makes for pretty simple code.
