# -*- coding: utf-8 -*-
import browser_cookie3, requests, re, json
from bs4 import BeautifulSoup

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

response = requests.get(url=url, cookies=cj, headers=headers)



print(cj)
print(url)

if response.status_code != 200:
        response.encoding = 'utf-8'
        print(response.status_code)
        print('ERROR')
else:
    soup = BeautifulSoup(response.text, 'lxml')
    boss_div = soup.find_all("div", class_=re.compile("boss-wrap"))

    boss_url = boss_div[0].a['href']

    boss_url = host + boss_url
    boss_response = requests.get(url=boss_url, cookies=cj, headers=headers)

    boss_soup = BeautifulSoup(boss_response.text, 'lxml')

    legal_list = boss_soup.find(id='legallist')

    legal_table = legal_list.table
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


    print(json.dumps(companay_json_list, indent=4, ensure_ascii=False))


    # invest_list = boss_soup.find(id='investlist')
    # invest_table = invest_list.table
    # for tr in invest_table.findAll('tr'):
    #     print('++++++row +++++++++++++++++++++++++')
    #     for td in tr.findAll('td'):
    #         print("---------")
    #         print(td.getText().replace(" ", "").replace("\t", "").strip())
