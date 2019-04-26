# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  return "" if a.empty?
  prefix = ''
  a[0].split('').each do |c|
      prefix += c
      unless a.map{ |w| w.include? prefix }.all?
        return prefix[0...-1]
      end
  end
end