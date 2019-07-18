from selenium import webdriver
import time

browser = webdriver.Firefox()
url="http://localhost/test.html"

browser.get(url)

page_id = 2

xpath = '//div[@id="legallist"]//a[@id="ajaxpage" and text() = "' + str(page_id) + '"]'
next_page = browser.find_element_by_xpath(xpath)

print(next_page.get_attribute('innerHTML'))

next_page.click()