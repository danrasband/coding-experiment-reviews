# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  x.abs.to_s.reverse.to_i * (x < 0 ? -1 : 1)
end