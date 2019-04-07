# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  return 0 if x.zero?
  x.to_s.split('').reverse.join.to_i * ( x / x.abs )
end
