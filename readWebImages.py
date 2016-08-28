#!/usr/bin/env python3

import time
import subprocess
from urllib.request import urlretrieve
from selenium import webdriver

# Create new Selenium driver
driver = webdriver.PhantomJS(executable_path="/usr/selenium/webdriver/phantomjs/phantomjs")
# when phantomjs has problems finding elements on this page, should try to
# use firefox with:
# driver = webdriver.Firefox()

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# Click on the book preview button
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# Wait for the page to load
time.sleep(5)

# While the right arrow is available for clicking, turn though pages
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # Get any new pages that have loaded (multiple pages can load at once,
    # but duplicates will not be added to a set)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

# Start processing the images we've collected URLs for with Tesseract
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    with open("page.txt", "r") as f:
        print(f.read())
