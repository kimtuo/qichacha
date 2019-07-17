from selenium import webdriver
import browser_cookie3, requests, re, json
from selenium import webdriver
import time

browser = webdriver.Firefox()

# browser.add_cookie(cj)
url = "https://www.qichacha.com/pl_p1910534b4ae98fea35ddbeb1d61cd44.html"
# url = "http://www.baidu.com/"

browser.get(url)
is_login = False
while True:
    try:
        if not is_login:
            login_link = browser.find_element_by_link_text('登录')
            print(login_link)
            print("------------------------------------------------------------------------------------")
            time.sleep(5)
    except Exception as e:
            print("Login!")
            is_login = True

    try:
        if is_login:
            next_page = browser.find_element_by_xpath('//div[@id="legallist"]//a[@id="ajaxpage" and text() = "2"]')
            print("click in 10 s")
            time.sleep(10)
            next_page.click()
            break
    except Exception as e:
        print(e)
        break
