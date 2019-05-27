# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  sum = 0
  (1..x).each do |num|
    if ((num/3).zero? || (num/5).zero?)
      sum += num
    end
  end
  return sum
end