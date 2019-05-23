# Feedback

## 1. Sum of Integers in a String

Nice, elegant solution here. The only problem is that the code doesn't check
for the empty string scenario, in which case it will fail.

## 2. Sum of Certain Multiples

It's an interesting idea to monkey-patch the Fixnum class. I'd recommend
against doing that in most scenarios. You may have just been trying to have
some fun, which is a totally valid reason to do that in this kind of setting.
I like how you've used the `Enumerable#select` and `Enumerable#inject` methods.
Nice job also ignoring the 0..2 cases at the beginning. You might have also
changed the `1.upto` to `3.upto`, but this is a nit-pick.

## 3. Longest Common Prefix

It looks like you ran out of time on this one. Nice try!
