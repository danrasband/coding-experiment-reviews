# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  table = a[0].split("")
  a.drop(1).each do |string|
    string.split("").each_with_index do |char, index|
      return "" if index == 0 && table[index] != char
      unless table[index] == char
        table = string.split("")[0...index]
        break
      end
    end
  end
  table.join("")
end