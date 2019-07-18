from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()
url="http://localhost/test.html"

print(time.time())

browser.get(url)

try:

    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "legallist"))
    )
    print(time.time())

    page_id = 2

    xpath = '//div[@id="legallist"]//a[@id="ajaxpage" and text() = "' + str(page_id) + '"]'
    next_page = browser.find_element_by_xpath(xpath)

    print(next_page.get_attribute('innerHTML'))

    next_page.click()


finally:
    browser.quit()

