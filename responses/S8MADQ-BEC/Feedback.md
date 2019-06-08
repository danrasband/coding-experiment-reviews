# Feedback

You chose an interesting approach to getting the max by starting with
<code>-2<sup>32</sup></code>. I like the thinking here. You could also start
with the first element in the array and go from there. One thing to note is
that <code>-2<sup>32</sup></code> is actually out of the range of a signed
32-bit integer. The low end of the range would be <code>-2<sup>31</sup></code>.

I would recommend using a linter to help improve your Python style.

Your solution to the longest common prefix is a cool approach, but a bit
overcomplicated. I don't see any reason to get that complicated with a pretty
simple programming problem. Maybe you were just having fun, and if that's the
case, that's a totally valid reason on a test like this.
