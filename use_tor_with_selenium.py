#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from selenium import webdriver
service_args = ['--proxy=localhost:9150', '--proxy-type=socks5']
driver = webdriver.PhantomJS(executable_path="/usr/selenium/webdriver/phantomjs/phantomjs")
driver.get("http://icanhazip.com")
print(driver.page_source)
driver.close()
