# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(s)
  return 0 if s.empty?
  s.split(',').map(&:to_i).reduce(:+)
end
