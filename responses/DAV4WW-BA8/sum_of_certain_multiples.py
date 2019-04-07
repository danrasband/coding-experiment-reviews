# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

class Fixnum
  def is_divisible_by(n)
    self%n == 0
  end

  def is_not_divisible_by(n)
    !is_divisible_by(n)
  end
end


def solution(x)
  return 0 if x <= 3
  1.upto(x-1)
    .select{ |e| (e.is_divisible_by(3) || e.is_divisible_by(5)) && e.is_not_divisible_by(15) }
    .inject(:+)
end
