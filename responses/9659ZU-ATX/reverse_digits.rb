# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  # write your code in Ruby
  converter_integer = x.to_s
  converter_integer[0].eql?('-') ? "-#{x.to_s.reverse}".to_i : x.to_s.reverse.to_i
  
end