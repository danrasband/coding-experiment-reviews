# Feedback

You may want to look at using a linter like pylint when you write your code to
level up your code style.

The solution to the first problem is pretty good. It's a bit verbose, since
you can just use `int()` to cast integer string to integers, but your solution
automatically handles the empty string case where the other doesn't.

In either case, I'd be careful about use an `if/elif` pattern without a final
`else`—it's easy to miss a case on accident that way.

It looks like you ran out of time on the third problem and the second was a bit
convoluted.
