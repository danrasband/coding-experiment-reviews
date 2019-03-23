def solution(a)
  return 0 if a.size.zero?

  max_int = a[0]
  count = 0

  a.each do |current|
    next count += 1 if max_int == current

    if current > max_int
      max_int = current
      count = 1
    end
  end

  count
end
