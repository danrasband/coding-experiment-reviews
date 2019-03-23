def solution(words)
  return '' if words.empty?
  return words[0] if words.size == 1

  prefix = words[0]

  words.each do |word|
    new_prefix = ''
    0.upto([[prefix.length, word.length].min - 1, 0].max).each do |i|
      break if prefix[i] != word[i]
      break if word.empty?

      new_prefix += word[i]
    end
    prefix = new_prefix
    break if prefix.empty?
  end

  prefix
end
