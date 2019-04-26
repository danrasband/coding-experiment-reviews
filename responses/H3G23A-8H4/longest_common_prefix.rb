# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x, b)
  return 0 if b.length == 0 || x > b.length
  
  c = b[0]
  d = b[1]
  b.each_with_index do |i, index|
    (index..x).each do  |j|
      if (b[index] * b[j] > c * d)
        c = b[index]
        d = b[j]
      end
    end
  end
  p c 
  p d
  c * d
end