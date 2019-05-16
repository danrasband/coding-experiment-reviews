# Feedback

## 1. Count of Largest Integer

This is an interesting approach. It would be a lot easier to simply loop over
the array, assuming the first element is the greatest, and keeping track of
the current count of the greatest number, resetting each time a greater
integer is found. Another approach would be to use the `.count` method and `max` function that Python provides out of the box.

## 2. Sum of Certain Multiples

Nice job with the `i % 15 != 0` technique. It is more idiomatic Python to use
`or` and `and` over `|` and `&`, but both work. Nice work overall!

## 3. Find Maximum Product

Nice work checking for edge cases from the get-go. There's no need for the
`else` clause since you're returning out of the first `if` clause. (Look up
"guard clauses".) Your solution is incorrect, though I'm guessing you probably
just ran out of time.

Nice work!
