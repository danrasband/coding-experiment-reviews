#!/usr/bin/env ruby
# frozen_string_literal: true

require 'rubygems'
require 'yaml'
require 'nokogiri'
require 'byebug'

TESTS = YAML.load(File.read('tests.yml'))
TEST_IDS = TESTS['test_ids']
TASKS = TESTS['tasks'].invert
TEST_CONFIGS = TESTS['test_configs']

def code_id(task_index, response_index)
  "pre#code-#{task_index}-#{response_index}"
end

def extract_code(test_id, task_name, task_index)
  html_file = "responses/#{test_id}/results.html"
  html = File.read(html_file)
  doc = Nokogiri::HTML(html)
  response_index = 0
  text = ''
  language_ext = 'py'

  loop do
    pre_tag = doc.css(code_id(task_index, response_index))
    break unless pre_tag.count.nonzero?
    text = pre_tag.text
    language_ext = pre_tag.css('code').first['data-prg-lang']
    response_index += 1
  end

  [text, language_ext]
rescue
  ['', 'py']
end

def write_code(test_id, task_name, language_ext, code)
  filename = 'responses/%s/%s.%s' % [test_id, task_name, language_ext]
  puts "Writing code to #{filename}"

  File.open(filename, 'w') do |fh|
    fh.write(code)
  end
end

TEST_IDS.each do |test_id, test_type|
  TEST_CONFIGS[test_type].each_with_index do |task_id, i|
    task_name = TASKS[task_id]
    code, language_ext = extract_code(test_id, task_name, i + 1)
    write_code(test_id, task_name, language_ext, code)
  end
end
