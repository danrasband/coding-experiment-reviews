# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x)
  reverse = 0
  sign = x < 0 ? -1 : 1
  number = x.abs
  while(number > 0) do
    last_digit = number % 10
    reverse = (reverse * 10) + last_digit
    number = number / 10
  end
  reverse * sign
end
