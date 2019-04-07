#!/usr/bin/env ruby -W

GOLDEN_DIR = 'golden'.freeze
RESPONSES_DIR = 'responses'.freeze

LANGUAGES = { javascript: :js, python: :py, ruby: :rb}.freeze

TEST_IDS = [
  # Week 1
  ['EC4GJT-SMK', :Platypus],
  ['9Z5UDF-ZEP', :Saiga],
  ['JQHT63-A6A', :Cassowary],
  ['RVM3S9-UP8', :Wombat],
  ['X352JA-RZM', :Platypus],
  ['58NJ7Z-URN', :Saiga],
  ['5AV2J9-5BS', :Cassowary],
  ['KT623X-42Q', :Wombat],
  ['MG7RGD-9R7', :Platypus],
  ['HH4HT2-UZB', :Saiga],
  ['YMFFGM-A3Q', :Cassowary],
  ['REK6D7-DGH', :Wombat],
  ['Q3A2XR-3VW', :Platypus],
  ['KSJC4D-8CY', :Saiga],
  ['PKEQCM-UXF', :Cassowary],
  ['ZTZQGJ-MQQ', :Wombat],
  ['8QRTD9-GGS', :Platypus],
  ['3JJAY9-8X9', :Saiga],
  ['UZRFMM-MY2', :Cassowary],
  ['EYG9HU-UHB', :Wombat],
  ['5PC7A3-VTC', :Platypus],
  ['9659ZU-ATX', :Saiga],
  ['4T59SN-Z8Q', :Cassowary],
  ['HKFE5Y-QSM', :Wombat],
  ['WFYFRM-9QS', :Platypus],
  ['3BHRPM-TK9', :Saiga],
  ['JZBZF7-KNE', :Cassowary],
  ['YXVDK8-JB4', :Wombat],
  ['CAXZU5-45T', :Platypus],

  # Week 2
  ['84QT7P-GSC', :Pangolin],
  ['T6CZBD-HJB', :Okapi],
  ['4BENHU-NUN', :Armadillo],
  ['M7BJS4-GTC', :Hyrax],
  ['79Z4TZ-8CG', :Pangolin],
  ['NYCS8Y-58S', :Okapi],
  ['A9KJ7K-GQ8', :Hyrax],
  ['DPCKN2-NF5', :Pangolin],
  ['G5F2NU-A3A', :Okapi],
  ['SJ7QK6-R4F', :Pangolin],
  ['WT4TZR-B3R', :Armadillo],
  ['SDXU35-KKU', :Hyrax],
  ['Z9S2T8-8XQ', :Pangolin],
  ['4N53A7-Z4R', :Okapi],
  ['AUS97P-NM9', :Armadillo],
  ['DAV4WW-BA8', :Hyrax],
  ['7A2QDT-RKD', :Pangolin],
  ['N7WCXZ-Y9Y', :Okapi],
  ['BWJ4RW-5Q8', :Armadillo],
  ['YJEH95-JPQ', :Hyrax],
  ['GPAUWQ-R8E', :Pangolin],
  ['FP3ANE-JEK', :Okapi],
  ['P535GE-KY8', :Armadillo],
  ['TK75Q6-7YJ', :Hyrax],
  ['4PCCCA-397', :Pangolin],
  ['QFB7HE-A7D', :Armadillo],
].freeze

TASKS = {
  1 => 'count_of_largest_integer',
  2 => 'sum_of_integers_in_a_string',
  3 => 'sum_of_certain_multiples',
  4 => 'reverse_digits',
  5 => 'longest_common_prefix',
  6 => 'find_maximum_product',
}.freeze

TEST_TYPES = {
  Platypus: [1, 3, 5],
  Wombat: [1, 4, 6],
  Saiga: [1, 4, 5],
  Cassowary: [1, 3, 6],
  Pangolin: [2, 4, 6],
  Okapi: [2, 3, 6],
  Armadillo: [2, 4, 5],
  Hyrax: [2, 3, 5],
}.freeze

def current_dir
  File.expand_path(File.dirname(__FILE__))
end

def responses_directory(test_id)
  File.join(current_dir, RESPONSES_DIR, test_id)
end

def golden_directory(language)
  File.join(current_dir, GOLDEN_DIR, language.to_s)
end

def make_directory(path)
  puts "Making directory: #{path}"
  Dir.mkdir(path)
  true
rescue StandardError
  false
end

def touch(path)
  File.open(path, 'a') {}
end

def make_files(test_id, test_type)
  dir = responses_directory(test_id)
  puts "Touching file: #{File.join(dir, 'Feedback.md')}"
  touch File.join(dir, 'Feedback.md')
  TEST_TYPES[test_type].each do |task_id|
    puts "Touching file: #{File.join(dir, "#{TASKS[task_id]}.py")}"
    touch File.join(dir, "#{TASKS[task_id]}.py")
  end
end

TEST_IDS.each do |(test_id, test_type)|
  make_files(test_id, test_type) if make_directory(responses_directory(test_id))
end

LANGUAGES.keys.each do |language|
  make_directory(golden_directory(language))
end

TASKS.each do |_, name|
  LANGUAGES.each do |language, extension|
    touch File.join(golden_directory(language), "#{name}.#{extension}")
  end
end
