# Feedback

## 1. Sum of Integers in a String

Excellent solution. One possible minor improvement (which isn't even shown in
our "golden" solution in Ruby) could be to remove the return guard clause,
remove the map, and change the reduce:

```ruby
def solution(s)
  s.split(',').reduce(0) { |a, e| a + int(e) }
end
```

Using the initial value of `0` in the reduce eliminates the need for the
initial return guard clause and using the `int(e)` within the reduce clause
eliminates the need for an extra `.map` iteration. This is super nit-picky,
though. Excellent job.

## 2. Reverse Digits

It was an interesting choice to check for 0 and use division to decide on the
sign. I think it's probably more performant to check for the sign beforehand,
then multiplying by +/- 1 after reversing and casting to an integer. Using
division _is_ clever, though. I don't think I would have come up with that.

## 3. Longest Common Prefix

This definitely works (nice job!), but a more performant way of doing this is
to simply assume that the first element of the array _is_ the longest common
prefix already, and then adjust that belief by shortening that string as
necessary as you compare it against each subsequent string in the array.
