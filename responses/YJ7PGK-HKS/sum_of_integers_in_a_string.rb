# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  answer = 0
  counter = Hash.new { 0 }
  
  a.each do |value|
    counter[value] += 1
    
    answer = counter[value] if counter[value] > answer
  end
  
  return answer
end
