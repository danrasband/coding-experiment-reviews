# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  sum = 0
  (1...x).each do |element|
    next if element % 3 != 0 && element % 5 != 0
    next if element % 3 == 0 && element % 5 == 0
      
    sum += element
  end
  sum
end