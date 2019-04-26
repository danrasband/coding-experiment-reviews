# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"
s = '1,0,-1'
def solution(s)
  sum = 0;
  s.split(',').each do |integer|
    sum += integer.to_i
  end
  return sum
end