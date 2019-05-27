# Feedback

## 1. Sum of Integers in a String

This is a good solution. There is an empty string scenario that this code
fails to check for, but otherwise it does the job.

## 2. Sum of Certain Multiples

This problem had an ambiguity that caused you to have an issue in your
solution. It should have said to not count numbers that were multiples of 15
because they are multiples of both three and five. Nice use of `sum` here. To
be more performant, you could just add things up as you go instead of saving
the elements in an array and summing them after you had collected them all.
