#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/usr/selenium/webdriver/phantomjs/phantomjs')
driver.get("http://www.xjr7670.com")
driver.get_screenshot_as_file("/tmp/xjr7670.com.png")

driver.close()
