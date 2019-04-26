# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  numbers = []
  1.upto(x) do |i|
    if (i%3).zero? ^ (i%5).zero?
      numbers.push i
    end
  end
  numbers.reduce(:+)
end