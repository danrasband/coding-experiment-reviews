def solution(x)
  sign = x < 0 ? -1 : 1

  x.abs.to_s.reverse.to_i * sign
end
