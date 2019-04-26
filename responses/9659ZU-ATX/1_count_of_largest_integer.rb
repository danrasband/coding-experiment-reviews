# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby
  grouped_array = a.group_by(&:itself).values
  grouped_array.max_by(&:length).count
end