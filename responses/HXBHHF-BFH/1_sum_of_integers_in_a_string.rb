# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  return 0 if a.empty?
  sorted_hash = a.sort.group_by { |x| x }
  sorted_hash.values.last.count
end