# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def prefix_len(s, t)
  len = 0

  while len < s.size && len < t.size && s[len] == t[len]
    len += 1
  end

  len
end

def solution(a)
  a = a.sort
  prefix_len = (1...(a.size)).map { |i| prefix_len(a[i-1], a[i]) }.min

  a[0][0, prefix_len]
end
