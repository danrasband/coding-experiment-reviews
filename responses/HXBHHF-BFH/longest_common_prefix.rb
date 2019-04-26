# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x, b)
  return 0 if b.empty? || x > b.size
  sorted_arr = b.sort
  sorted_arr[-x..-1].reduce(:*)
end