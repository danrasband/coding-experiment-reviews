# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  return 0 if a.length == 0
  hash_table = {}
  a.each do |element|
    if hash_table[element]
      hash_table[element] += 1
    else
      hash_table[element] = 1
    end
  end
  hash_table.values.max
end