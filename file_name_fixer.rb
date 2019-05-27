#!/usr/bin/env ruby -W
# frozen_string_literal: true

require 'rubygems'
require 'yaml'
require 'nokogiri'
require 'byebug'
require 'shellwords'

TESTS = YAML.load(File.read('tests.yml'))
TEST_IDS = TESTS['test_ids'].keys
TASKS = TESTS['tasks'].invert
TEST_CONFIGS = TESTS['test_configs']
PER_TEST_CONFIG = TESTS['test_ids']

TEST_IDS.each do |test_id|
  directory = "responses/#{test_id}"
  week = PER_TEST_CONFIG[test_id]['Week']
  task_offset = week == 2 ? 3 : 0
  tasks = TEST_CONFIGS[PER_TEST_CONFIG[test_id]['TestName']].slice(0 + task_offset, 3)

  tasks.each_with_index do |task_id, i|
    task_number = i + 1
    file = Dir.glob("#{directory}/#{task_number}_*").first
    next unless file

    task_name = TASKS[task_id]
    extension = File.extname(file)
    intended_file_name = "#{directory}/#{task_number}_#{task_name}#{extension}"
    next if file == intended_file_name

    cmd = "mv #{file.shellescape} #{intended_file_name.shellescape}"
    system(cmd)
  end
end

