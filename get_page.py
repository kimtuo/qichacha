from selenium import webdriver
import time

browser = webdriver.Firefox()
url="http://localhost/test.html"

browser.get(url)
next_page = browser.find_element_by_xpath('//div[@id="legallist"]//a[@id="ajaxpage" and text() = "2"]')

print(next_page.get_attribute('innerHTML'))

next_page.click()