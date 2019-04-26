# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def sum_first_n(n)
  n * (n + 1) / 2
end

def solution(x)
  three_count = (x - 1) / 3
  five_count = (x - 1) / 5
  fifteen_count = (x - 1) / 15
  
  three = 3 * sum_first_n(three_count)
  five = 5 * sum_first_n(five_count)
  fifteen = 15 * sum_first_n(fifteen_count)
  
  three + five - 2 * fifteen
end
