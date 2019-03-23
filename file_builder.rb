#!/usr/bin/env ruby -W

RESPONSES_DIR = 'responses'.freeze

TEST_IDS = [
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

def directory(test_id)
  File.join(File.expand_path(File.dirname(__FILE__)), RESPONSES_DIR, test_id)
end

def make_directory(test_id)
  dir = directory(test_id)
  puts "Making directory: #{dir}"
  Dir.mkdir(directory(test_id))
  true
rescue StandardError
  false
end

def touch(path)
  File.open(path, 'a') {}
end

def make_files(test_id, test_type)
  dir = directory(test_id)
  puts "Touching file: #{File.join(dir, 'Feedback.md')}"
  touch File.join(dir, 'Feedback.md')
  TEST_TYPES[test_type].each do |task_id|
    puts "Touching file: #{File.join(dir, "#{TASKS[task_id]}.py")}"
    touch File.join(dir, "#{TASKS[task_id]}.py")
  end
end

TEST_IDS.each do |(test_id, test_type)|
  make_files(test_id, test_type) if make_directory(test_id)
end
