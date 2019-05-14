# Feedback

## 1. Count of Largest Integer

Nice job on the documentation of your function, and nice work checking for the
edge cases from the get-go. A couple of things would have simplified your code
immensely:

1. Since the test gives assumptions as to what the function will receive, you
don't need to do the checking for bad inputs.
2. You can loop through `A` only once and keep a memo of the highest integer you've seen to date, along with a memo of its count.

Again, I'm really impressed by the thoroughness of your comments.

## 2. Sum of Certain Multiples

Again, no need to check for bad inputs. Looping through the numbers backwards
is an interesting approach. Some ES6 coding patterns could have improved your
code a bit (see the "golden" response [here](https://github.com/danrasband/coding-experiment-reviews/blob/master/golden/javascript/2_sum_of_certain_multiples.js).

## 3. Longest Common Prefix

No worries that you didn't finish! 30 minutes isn't much time at all!
