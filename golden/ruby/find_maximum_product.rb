def solution(x, b)
  return 0 if b.empty?
  return 0 if x > b.size
  return b[0] if b.size == 1

  max = 0

  (x).upto(b.size) do |right_index|
    window = b[right_index - x...right_index]
    prod = window.reduce(1) { |a, e| a * e }
    max = prod if max < prod
  end

  max
end
