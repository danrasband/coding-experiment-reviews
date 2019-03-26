# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  shortest = a.min_by &:length
  maxlen = shortest.length
  maxlen.downto(0) do |len|
    0.upto(maxlen - len) do |start|
      substr = shortest[start,len]
      return substr if a.all?{|str| str.include? substr }
    end
  end
end
