# Feedback

## 1. Count of Largest Integer

This is a very typical approach for getting the max, and one I would have used
before. It's not the most performant, however, because you have to count
everything, then find the largest count, then get the value that has that
largest count. There's a more performant approach that allows you to go through
the array just once. See [the example solution](https://github.com/danrasband/coding-experiment-reviews/blob/master/golden/python/1_count_of_largest_integer.py).
Another approach that is good because of its conciseness, if not performance, can be seen [here](https://github.com/danrasband/coding-experiment-reviews/blob/master/responses/HKFE5Y-QSM/1_count_of_largest_integer.py).

Lastly, while the names you chose for variables wasn't wrong, I often prefer
using more semantically informative variables. This helps with understanding
each of their purposes, which can be helpful when coming back to code several
months after first writing it.

## 2. Reverse Digits

Nice job working this out in such a short time frame. Some things that might
improve your code are 1) the `.reverse()` method on the list class instance
and 2) checking the sign of the integer before converting it to a string.
