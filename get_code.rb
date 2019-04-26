#!/usr/bin/env ruby
# frozen_string_literal: true

require 'rubygems'
require 'mechanize'
require 'dotenv'
require 'yaml'

Dotenv.load

LOGIN_URL = 'https://app.codility.com/accounts/login/'
TICKET_URL_TEMPLATE = 'https://app.codility.com/tickets/%s/'
USER_AGENT = 'UC Berkeley W241 Experiment Code Scraper/V0.1'
TESTS = YAML.load(File.read('test.yml'))
TICKETS = TESTS['test_ids'].keys

def agent
  @agent ||= Mechanize.new do |config|
    config.user_agent = USER_AGENT
  end
end

def login
  agent.get(LOGIN_URL) do |page|
    page.form_with(id: 'login-form') do |login_form|
      login_form.username = ENV['CODILITY_USERNAME']
      login_form.password = ENV['CODILITY_PASSWORD']
    end.submit
  end
end

def retrieve_ticket_html(ticket)
  url = TICKET_URL_TEMPLATE % ticket

  file = agent.get(url)
  filename = 'responses/%s/results.html' % ticket
  file.save!(filename)
end

login
TICKETS.each do |ticket|
  retrieve_ticket_html(ticket)
end
