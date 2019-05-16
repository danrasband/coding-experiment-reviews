# Feedback

## 1. Count of Largest Integer

I think you missed the point a little bit on this one. You should have found
the count of the maximum integer. So, if there are [1,2,3,2,1], the count is
1, since 3 is the max.

Interesting choice to use `.group_by(&:itself)` and `.max_by(&:itself)`. I've
never seen those patterns in all my years of Ruby development.

## 2. Reverse Digits

This is a cool solution. I like how simple Ruby makes it. You could make it
even simpler like this:

```ruby
sign = x < 0 ? -1 : 1
x.abs.to_s.reverse.to_i * sign
```

## 3. Longest Common Prefix

A more performant way of tackling this problem is to assume the first element
of the array is the longest common prefix, then adjust your understanding of
what's the longest as you walk through the rest of the array. I do like the
way you're thinking here, though.
