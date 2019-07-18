# -*- coding: utf-8 -*-
import browser_cookie3, requests, re, json
from bs4 import BeautifulSoup
from selenium import webdriver
import time

cj = browser_cookie3.firefox()

host = "https://www.qichacha.com"

key = "雷军"
url = "https://www.qichacha.com/search?key=" + key



headers = {
'Host':'www.qichacha.com',
'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
'Accept':'*/*',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Referer':'http://www.qichacha.com/',
'Cache-Control':'max-age=0',
}



#
#
# print(cj)
# print(url)

# if response.status_code != 200:
#         response.encoding = 'utf-8'
#         print(response.status_code)
#         print('ERROR')
# else:

def parse_company(html):

    # boss_response = requests.get(url=boss_url, cookies=cj, headers=headers)

    print("----------------parse company--------------------------")

    boss_soup = BeautifulSoup(html, 'lxml')

    legal_list = boss_soup.find(id='legallist')

    legal_table = legal_list.table

    print("----------------get legal_list table--------------------------")

    company_list = []
    for tr in legal_table.findAll('tr'):
        tb_list = []
        for td in tr.findAll('td'):
            if td.getText() is not None:
                tb_list.append(td.getText().replace(" ","").replace("\t","").strip())
            if td.a is not None:
                tb_list.append(td.a['href'])

        if len(tb_list) != 0:
            company_list.append(tb_list)

    print("----------------get table data to list--------------------------")

    companay_json_list = []
    for c in company_list:
        json_data = {}
        json_data['id'] = c[0]
        json_data['company_name'] = c[1]
        json_data['company_url'] = c[2]
        json_data['invest_percent'] = c[3]
        json_data['invest_sum'] = c[4]
        json_data['location'] = c[5]
        json_data['scope'] = c[6]
        json_data['status'] = c[7]

        companay_json_list.append(json_data)

    # print(json.dumps(companay_json_list, indent=4, ensure_ascii=False))

    return companay_json_list

    # invest_list = boss_soup.find(id='investlist')
    # invest_table = invest_list.table
    # for tr in invest_table.findAll('tr'):
    #     print('++++++row +++++++++++++++++++++++++')
    #     for td in tr.findAll('td'):
    #         print("---------")
    #         print(td.getText().replace(" ", "").replace("\t", "").strip())


key = "雷军"
url = "https://www.qichacha.com/search?key=" + key
# url = "http://www.baidu.com/"
browser = webdriver.Firefox()

response = requests.get(url=url, cookies=cj, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
boss_div = soup.find_all("div", class_=re.compile("boss-wrap"))
boss_url = boss_div[0].a['href']
boss_url = host + boss_url


browser.get(boss_url)
companay_json_list=[]

is_login = False
while True:
    try:
        if not is_login:
            login_link = browser.find_element_by_link_text('登录')
            print("--请扫码登录--")
            print("------------------------------------------------------------------------------------")
            time.sleep(5)
    except Exception as e:
            print("Login!")
            is_login = True

    try:
        if is_login:
            boss_page_soup = BeautifulSoup(browser.page_source, 'lxml')
            com_count = boss_page_soup.find_all('span', class_='tbadge')[0].getText().replace(" ", "").replace("\t", "").strip()

            page_count = int(com_count)//10 + 1
            print(int(page_count))

            company_json_list = parse_company(browser.page_source)

            if page_count > 1:
                for p in range(1, page_count):
                    page_id = p + 1
                    xpath = '//div[@id="legallist"]//a[@id="ajaxpage" and text() = "' + str(page_id) + '"]'
                    next_page = browser.find_element_by_xpath(xpath=xpath)
                    print("Now going to next page :")
                    print(xpath)

                    next_page.click()
                    time.sleep(5)

                    this_com_list = parse_company(browser.page_source)
                    company_json_list.extend(this_com_list)

                    # print("+++++++++++++++++++++++This List++++++++++++++++++++")
                    # print(json.dumps(this_com_list, indent=4, ensure_ascii=4))
                    # print("+++++++++++++++++++++++This List++++++++++++++++++++")

            print(json.dumps(company_json_list, indent=4, ensure_ascii=False))
            break

    except Exception as e:
        print(e)
        break
