# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(s)
  s.split(",").inject(0) do |sum, number|
    sum += number.to_i
  end
end
