def solution(s)
  s.split(',').map(&:to_i).reduce(0) { |a, e| a + e }
end
