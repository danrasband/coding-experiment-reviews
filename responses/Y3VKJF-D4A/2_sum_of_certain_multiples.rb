# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
l = m = 0

while x > 0 do 

m = m + x if x%5 == 0 && !x.eql?(5)
l = l + x if x%3 == 0 && !x.eql?(3)
x -=1
end


l+m
end