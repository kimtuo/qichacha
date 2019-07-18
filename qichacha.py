
# -*- coding: utf-8 -*-
import browser_cookie3, requests, re, json
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Qichacha():

    def __init__(self):
        self.cj = browser_cookie3.firefox()
        self.host = "https://www.qichacha.com"
        self.base_url = "https://www.qichacha.com/search?key="

        self.headers = {
            'Host': 'www.qichacha.com',
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.qichacha.com/',
            'Cache-Control': 'max-age=0',
        }

    def parse_company(self, html):

        # boss_response = requests.get(url=boss_url, cookies=cj, headers=headers)
        # print("----------------parse company--------------------------")
        boss_soup = BeautifulSoup(html, 'lxml')
        legal_list = boss_soup.find(id='legallist')
        legal_table = legal_list.table
        # print("----------------get legal_list table--------------------------")

        company_list = []
        for tr in legal_table.findAll('tr'):
            tb_list = []
            for td in tr.findAll('td'):
                if td.getText() is not None:
                    tb_list.append(td.getText().replace(" ", "").replace("\t", "").strip())
                if td.a is not None:
                    tb_list.append(td.a['href'])

            if len(tb_list) != 0:
                company_list.append(tb_list)
        # print("----------------get table data to list--------------------------")

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

    def find_company_by_person(self, person):
        url = self.base_url + person
        response = requests.get(url=url, cookies=self.cj, headers=self.headers)

        if response.status_code != 200:
            response.encoding = 'utf-8'
            print(response.status_code)
            print('ERROR')
            return []
        else:
            soup = BeautifulSoup(response.text, 'lxml')
            boss_div = soup.find_all("div", class_=re.compile("boss-wrap"))
            boss_url = boss_div[0].a['href']
            boss_url = self.host + boss_url
            browser = webdriver.Firefox()
            browser.get(boss_url)

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
                        com_count = boss_page_soup.find_all('span', class_='tbadge')[0].getText().replace(" ","").replace("\t", "").strip()
                        page_count = int(com_count) // 10 + 1
                        company_json_list = self.parse_company(browser.page_source)

                        if page_count > 1:
                            for p in range(1, page_count):
                                page_id = p + 1
                                xpath = '//div[@id="legallist"]//a[@id="ajaxpage" and text() = "' + str(page_id) + '"]'
                                next_page = browser.find_element_by_xpath(xpath=xpath)
                                print("Now going to next page :")

                                next_page.click()
                                time.sleep(5)

                                this_com_list = self.parse_company(browser.page_source)
                                company_json_list.extend(this_com_list)

                                # print("+++++++++++++++++++++++This List++++++++++++++++++++")
                                # print(json.dumps(this_com_list, indent=4, ensure_ascii=4))
                                # print("+++++++++++++++++++++++This List++++++++++++++++++++")
                        print(json.dumps(company_json_list, indent=4, ensure_ascii=False))
                        return company_json_list
                except Exception as e:
                    print(e)
                    break
        return []

    def get_company_info_from_json_list(self, companay_json_list):

        result_list = []
        try:

            for company in companay_json_list:
                url = self.host + company['company_url']
                # print("Trying : " + url)
                response = requests.get(url=url, cookies=self.cj, headers=self.headers)
                if response.status_code != 200:
                    response.encoding = 'utf-8'
                    print(response.status_code)
                    print('ERROR')
                    return []
                else:
                    soup = BeautifulSoup(response.text, 'lxml')
                    # 企业信息
                    # print("-----------------------code-------------------")
                    try:
                        company_code_soup = soup.find_all("td", class_='tb', text="统一社会信用代码")[0].findNext('td')
                        company_code = company_code_soup.getText().replace(" ", "").replace("\t", "").strip()
                    except Exception as e:
                        print(e)
                        company_code = "xxx"

                    # 股东信息
                    # print("------------get partner-------------")
                    partner_list = []
                    partner = soup.find_all(id="partnerslist")[0].table
                    for tr in partner.findAll('tr'):
                        tb_list = []
                        for td in tr.findAll('td'):

                            if td.a is not None and td.a.getText().replace(" ", "").replace("\t", "").strip() != "持股详情>":
                                tb_list.append(td.a.getText().replace(" ", "").replace("\t", "").strip())
                            else:
                                if td.getText() is not None:
                                    tb_list.append(
                                        td.getText().replace(" ", "").replace("\t", "").replace("\n", "").replace("持股详情>", "").strip())
                        if len(tb_list) > 3 :
                            partner_list.append(tb_list)

                    print("------------------partner list--------------------")
                    print(partner_list)

                    partner_json_list = []
                    for p in partner_list:
                        if p is not None:
                            json_data = {}
                            json_data['id'] = p[0]
                            json_data['partner_name'] = p[1]
                            json_data['percent'] = p[4]
                            json_data['invest_count'] = p[5]
                            json_data['invest_date'] = p[6]
                            partner_json_list.append(json_data)

                    print("------------get member-------------")
                    # 成員信息
                    member_list = []
                    member_soup = soup.find_all(id="Mainmember")
                    if len(member_soup) > 0:
                        member = soup.find_all(id="Mainmember")[0].table
                        for tr in member.findAll('tr'):
                            tb_list = []
                            for td in tr.findAll('td'):
                                if td.a is not None:
                                    tb_list.append(td.a.getText().replace(" ", "").replace("\t", "").strip())
                                else:
                                    if td.getText() is not None:
                                        tb_list.append(
                                            td.getText().replace(" ", "").replace("\t", "").replace("\n", "").strip())

                            if len(tb_list) != 0:
                                member_list.append(tb_list)


                    # print(member_list)

                    member_json_list = []
                    for p in member_list:
                        if p is not None:
                            json_data = {}
                            json_data['id'] = p[0]
                            json_data['partner_name'] = p[1]
                            json_data['title'] = p[2]
                            member_json_list.append(json_data)

                    # print("get company name")
                    company_name = soup.find_all('h1')[0].getText()

                    company_json = {}
                    company_json['company_name'] = company_name
                    company_json['company_code'] = company_code
                    company_json['member'] = member_json_list
                    company_json['partner'] = partner_json_list

                    # print(json.dumps(company_json, indent=4, ensure_ascii=False))
                    result_list.append(company_json)
        except Exception as e:
            print(company)
            print(e)

        return result_list


if __name__ == '__main__':
    check_company_list = []
    check_person_list = []
    company_result = []

    # person = input("请输入要查找的人名： ")
    person = "雷军"
    qichacha = Qichacha()


    def check_name(person):
        c_list = qichacha.find_company_by_person(person)
        result = qichacha.get_company_info_from_json_list(c_list)
        return result

    if person not in check_person_list:
        check_person_list.append(person)
        result = check_name(person)
        print(json.dumps(result, indent=4, ensure_ascii=False))
