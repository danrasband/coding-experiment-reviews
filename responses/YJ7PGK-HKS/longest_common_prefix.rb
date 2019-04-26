# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x, b)
  return 0 if x > b.size
  return 0 if x < 0
  return 1 if x == 0
  
  return (0 .. (b.size - x)).to_a.map { |i| b[i, x].reduce(&:*) }.max
end
