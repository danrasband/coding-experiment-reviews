#!/usr/bin/env ruby -W

require 'yaml'

GOLDEN_DIR = 'golden'.freeze
RESPONSES_DIR = 'responses'.freeze

LANGUAGES = { javascript: :js, python: :py, ruby: :rb }.freeze

TESTS = YAML.load(File.read('tests.yml'))
TEST_IDS = TESTS['test_ids']
TASKS = TESTS['tasks'].invert
TEST_CONFIGS = TESTS['test_configs']

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
  TEST_CONFIGS[test_type].each do |task_id|
    puts "Touching file: #{File.join(dir, "#{TASKS[task_id]}.py")}"
    touch File.join(dir, "#{TASKS[task_id]}.py")
  end
end

TEST_IDS.each do |test_id, test_type|
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
