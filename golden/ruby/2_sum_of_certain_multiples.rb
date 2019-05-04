def solution(x)
  match = ->(i) { i % 15 != 0 && (i % 3 == 0 || i % 5 == 0) }
  integers = (0...x).to_a.select { |i| match.call(i) }
  return 0 if integers.empty?
  integers.reduce(0) { |a, e| a + e }
end
