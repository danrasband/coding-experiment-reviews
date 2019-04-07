# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  str = ''
  a.each do |item|
    i = 0
    while i < item.length
      matched = 0

      a.each do |string|
        matched += 1 if string.include?(str)
      end

      if matched == a.length && i > 0
        str += item[i-1]
      else
        break
      end
      i += 1
    end
  end
  return str
end
