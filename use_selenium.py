#!/usr/bin/env python3

import time
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\Python34\selenium\webdriver\phantomjs\bin\phantomjs.exe')
driver.get("http://www.pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()
