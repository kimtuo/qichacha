# -*- coding: utf-8 -*-
import browser_cookie3, requests, re, json
from bs4 import BeautifulSoup

cj = browser_cookie3.firefox()

host = "https://www.qichacha.com"

key = "雷军"
url = "https://www.qichacha.com/firm_91646522c6a3d38e376905f542056a5c.html"

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

    #企业信息
    # print("-----------------------code-------------------")
    company_code_soup = soup.find_all("td", class_='tb', text="统一社会信用代码")[0].findNext('td')
    company_code = company_code_soup.getText().replace(" ", "").replace("\t", "").strip()

    #股东信息
    partner_list = []
    partner = soup.find_all(id="partnerslist")[0].table
    for tr in partner.findAll('tr'):
        tb_list = []
        for td in tr.findAll('td'):
            if td.a is not None:
                tb_list.append(td.a.getText().replace(" ", "").replace("\t", "").strip())
            else:
                if td.getText() is not None:
                    tb_list.append(td.getText().replace(" ","").replace("\t","").replace("\n","").strip())

        if len(tb_list) > 3 :
            print(tb_list)
            partner_list.append(tb_list)


    partner_json_list = []
    for p in partner_list:
        json_data = {}
        json_data['id'] = p[0]
        json_data['partner_name'] = p[1]
        json_data['percent'] = p[4]
        json_data['invest_count'] = p[5]
        json_data['invest_date'] = p[6]
        partner_json_list.append(json_data)

    # 股东信息
    member_list = []
    member = soup.find_all(id="Mainmember")[0].table
    for tr in member.findAll('tr'):
        tb_list = []
        for td in tr.findAll('td'):

            if td.a is not None:
                tb_list.append(td.a.getText().replace(" ", "").replace("\t", "").strip())
            else:
                if td.getText() is not None:
                    tb_list.append(td.getText().replace(" ", "").replace("\t", "").replace("\n", "").strip())

        if len(tb_list) != 0:
            member_list.append(tb_list)

    member_json_list = []
    for p in member_list:
        json_data = {}
        json_data['id'] = p[0]
        json_data['partner_name'] = p[1]
        json_data['title'] = p[2]

        member_json_list.append(json_data)


    company_name = soup.find_all('h1')[0].getText()

    company_json = {}
    company_json['company_name'] = company_name
    company_json['company_code'] = company_code
    company_json['member'] = member_json_list
    company_json['partner'] = partner_json_list

    print(json.dumps(company_json, indent=4, ensure_ascii=False))

