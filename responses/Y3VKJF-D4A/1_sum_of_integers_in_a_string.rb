# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(s)
  # write your code in Ruby
  a = s.split(',')
d = 0  
a.each{|b| d = d  + b.to_i}
d
end