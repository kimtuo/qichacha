import csv

a = [
    {
        "id": "1",
        "company_name": "小米科技有限责任公司",
        "company_url": "/firm_9cce0780ab7644008b73bc2120479d31.html",
        "invest_percent": "77.8%",
        "invest_sum": "185000万元人民币",
        "location": "北京市",
        "scope": "科学研究和技术服务业",
        "status": "在业"
    },
    {
        "id": "2",
        "company_name": "拉萨经济技术开发区顺为资本投资咨询有限公司",
        "company_url": "/firm_fb0989a376b388a8d35b385ae40cf458.html",
        "invest_percent": "75%",
        "invest_sum": "10000万元人民币",
        "location": "西藏自治区",
        "scope": "租赁和商务服务业",
        "status": "存续"
    },
    {
        "id": "3",
        "company_name": "北京顺为创业投资有限公司",
        "company_url": "/firm_ac66f9d18c12d884e23b7c83bbad1c6b.html",
        "invest_percent": "51%",
        "invest_sum": "3000万元人民币",
        "location": "北京市",
        "scope": "租赁和商务服务业",
        "status": "在业"
    },
    {
        "id": "4",
        "company_name": "拉萨经济技术开发区顺创资本管理有限公司",
        "company_url": "/firm_b084d232b24e473a7d3554de9c36e9a8.html",
        "invest_percent": "33%",
        "invest_sum": "3万元人民币",
        "location": "西藏自治区",
        "scope": "租赁和商务服务业",
        "status": "存续"
    },
    {
        "id": "5",
        "company_name": "武汉顺创股权投资管理有限责任公司",
        "company_url": "/firm_c38f7bc7bf172cb3b626c6d1dea68d3c.html",
        "invest_percent": "33%",
        "invest_sum": "100万元人民币",
        "location": "湖北省",
        "scope": "租赁和商务服务业",
        "status": "存续"
    },
    {
        "id": "6",
        "company_name": "四川银米科技有限责任公司",
        "company_url": "/firm_006f4aa686287cb359b449ce6ce347d1.html",
        "invest_percent": "-",
        "invest_sum": "200000万元人民币",
        "location": "四川省",
        "scope": "科学研究和技术服务业",
        "status": "存续"
    },
    {
        "id": "7",
        "company_name": "广东小米科技有限责任公司",
        "company_url": "/firm_02ff6e6bed57a655db1bc67dfa829984.html",
        "invest_percent": "-",
        "invest_sum": "100000万元人民币",
        "location": "广东省",
        "scope": "信息传输、软件和信息技术服务业",
        "status": "在业"
    },
    {
        "id": "8",
        "company_name": "小米科技(武汉)有限公司",
        "company_url": "/firm_3fc8e6b450a351dffaf97ebba7bd5675.html",
        "invest_percent": "-",
        "invest_sum": "21000万元人民币",
        "location": "湖北省",
        "scope": "科学研究和技术服务业",
        "status": "存续"
    },
    {
        "id": "9",
        "company_name": "北京顺为资本投资咨询有限公司",
        "company_url": "/firm_f2117188041ae557029558232f8cbb6c.html",
        "invest_percent": "-",
        "invest_sum": "50万美元",
        "location": "北京市",
        "scope": "租赁和商务服务业",
        "status": "在业"
    },
    {
        "id": "10",
        "company_name": "捷付睿通股份有限公司",
        "company_url": "/firm_fb9c28e66da9cf101cd174bf27c97b3a.html",
        "invest_percent": "-",
        "invest_sum": "10000万元人民币",
        "location": "内蒙古自治区",
        "scope": "信息传输、软件和信息技术服务业",
        "status": "存续"
    },
    {
        "id": "11",
        "company_name": "西藏小米科技有限责任公司",
        "company_url": "/firm_ad622acd512e8f07fb287627b6901a7d.html",
        "invest_percent": "-",
        "invest_sum": "100万元人民币",
        "location": "西藏自治区",
        "scope": "批发和零售业",
        "status": "注销"
    },
    {
        "id": "12",
        "company_name": "天津顺米投资有限公司",
        "company_url": "/firm_ccac05966733d0e157ce3ab2e11eebca.html",
        "invest_percent": "-",
        "invest_sum": "10000万元人民币",
        "location": "天津市",
        "scope": "金融业",
        "status": "注销"
    }
]


b = [
    {
        "company_name": "小米科技有限责任公司",
        "company_code": "91110108551385082Q",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "董事长,经理"
            },
            {
                "id": "2",
                "partner_name": "刘芹",
                "title": "董事"
            },
            {
                "id": "3",
                "partner_name": "林斌",
                "title": "董事"
            },
            {
                "id": "4",
                "partner_name": "许达来",
                "title": "董事"
            },
            {
                "id": "5",
                "partner_name": "黎万强",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "雷军",
                "percent": "77.80%",
                "invest_count": "143934.05",
                "invest_date": "2015-10-30"
            },
            {
                "id": "2",
                "partner_name": "黎万强",
                "percent": "10.12%",
                "invest_count": "18724.357",
                "invest_date": "2015-10-30"
            },
            {
                "id": "3",
                "partner_name": "洪锋",
                "percent": "10.07%",
                "invest_count": "18623.1",
                "invest_date": "2015-10-30"
            },
            {
                "id": "4",
                "partner_name": "刘德",
                "percent": "2.01%",
                "invest_count": "3718.4963",
                "invest_date": "2015-10-30"
            }
        ]
    },
    {
        "company_name": "拉萨经济技术开发区顺为资本投资咨询有限公司",
        "company_code": "915400913213656094",
        "member": [
            {
                "id": "1",
                "partner_name": "张彤",
                "title": "总经理"
            },
            {
                "id": "2",
                "partner_name": "雷军",
                "title": "执行董事"
            },
            {
                "id": "3",
                "partner_name": "曹莉平",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "雷军",
                "percent": "75.00%",
                "invest_count": "7500",
                "invest_date": "-"
            },
            {
                "id": "2",
                "partner_name": "张彤",
                "percent": "25.00%",
                "invest_count": "2500",
                "invest_date": "-"
            }
        ]
    },
    {
        "company_name": "北京顺为创业投资有限公司",
        "company_code": "91110108575193173H",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "经理,执行董事"
            },
            {
                "id": "2",
                "partner_name": "张彤",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "雷军",
                "percent": "51.00%",
                "invest_count": "510,1020",
                "invest_date": "2011-05-05,2012-07-03"
            },
            {
                "id": "2",
                "partner_name": "张彤",
                "percent": "49.00%",
                "invest_count": "490,980",
                "invest_date": "2011-05-05,2012-07-03"
            }
        ]
    },
    {
        "company_name": "拉萨经济技术开发区顺创资本管理有限公司",
        "company_code": "91540091MA6T13RE41",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "经理,执行董事"
            },
            {
                "id": "2",
                "partner_name": "曹莉平",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "马文静",
                "percent": "34.00%",
                "invest_count": "1.02",
                "invest_date": "2045-01-01"
            },
            {
                "id": "2",
                "partner_name": "雷军",
                "percent": "33.00%",
                "invest_count": "0.99",
                "invest_date": "2045-01-01"
            },
            {
                "id": "3",
                "partner_name": "曹莉平",
                "percent": "33.00%",
                "invest_count": "0.99",
                "invest_date": "2045-01-01"
            }
        ]
    },
    {
        "company_name": "武汉顺创股权投资管理有限责任公司",
        "company_code": "91420100MA4KYD6T9P",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "执行董事"
            },
            {
                "id": "2",
                "partner_name": "马文静",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "马文静",
                "percent": "34.00%",
                "invest_count": "34",
                "invest_date": "2068-04-01"
            },
            {
                "id": "2",
                "partner_name": "雷军",
                "percent": "33.00%",
                "invest_count": "33",
                "invest_date": "2068-04-01"
            },
            {
                "id": "3",
                "partner_name": "曹莉平",
                "percent": "33.00%",
                "invest_count": "33",
                "invest_date": "2068-04-01"
            }
        ]
    },
    {
        "company_name": "四川银米科技有限责任公司",
        "company_code": "91510100780132134U",
        "member": [
            {
                "id": "1",
                "partner_name": "洪锋",
                "title": "董事兼总经理"
            },
            {
                "id": "2",
                "partner_name": "雷军",
                "title": "董事长"
            },
            {
                "id": "3",
                "partner_name": "LINBIN",
                "title": "董事"
            },
            {
                "id": "4",
                "partner_name": "刘德",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "北京小米电子软件技术有限公司",
                "percent": "100%",
                "invest_count": "200000",
                "invest_date": "-"
            }
        ]
    },
    {
        "company_name": "广东小米科技有限责任公司",
        "company_code": "91440101MA59A5P606",
        "member": [
            {
                "id": "1",
                "partner_name": "刘德",
                "title": "经理"
            },
            {
                "id": "2",
                "partner_name": "雷军",
                "title": "执行董事"
            },
            {
                "id": "3",
                "partner_name": "洪锋",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "小米通讯技术有限公司",
                "percent": "100%",
                "invest_count": "100000",
                "invest_date": "2016-12-31"
            }
        ]
    },
    {
        "company_name": "小米科技(武汉)有限公司",
        "company_code": "91420100MA4KWE6L5W",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "执行董事兼总经理"
            },
            {
                "id": "2",
                "partner_name": "刘德",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "小米通讯技术有限公司",
                "percent": "100%",
                "invest_count": "21000",
                "invest_date": "-"
            }
        ]
    },
    {
        "company_name": "北京顺为资本投资咨询有限公司",
        "company_code": "911101055906395752",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "经理,执行董事"
            },
            {
                "id": "2",
                "partner_name": "马文静",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "ShunweiCapitalPartnersAdvisor(HK)Limited",
                "percent": "100%",
                "invest_count": "50",
                "invest_date": "2012-04-25,2014-01-24"
            }
        ]
    },
    {
        "company_name": "捷付睿通股份有限公司",
        "company_code": "91150100566916827X",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "董事长"
            },
            {
                "id": "2",
                "partner_name": "洪锋",
                "title": "总经理,董事"
            },
            {
                "id": "3",
                "partner_name": "刘德",
                "title": "董事"
            },
            {
                "id": "4",
                "partner_name": "武军",
                "title": "董事"
            },
            {
                "id": "5",
                "partner_name": "郭娇阳",
                "title": "董事"
            },
            {
                "id": "6",
                "partner_name": "祁燕",
                "title": "监事"
            },
            {
                "id": "7",
                "partner_name": "刘媛",
                "title": "监事"
            },
            {
                "id": "8",
                "partner_name": "刘荣",
                "title": "监事会主席"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "呼和浩特市盛银和睿科技有限责任公司",
                "percent": "97.00%",
                "invest_count": "9700",
                "invest_date": "-"
            },
            {
                "id": "2",
                "partner_name": "刘荣",
                "percent": "2.00%",
                "invest_count": "200",
                "invest_date": "-"
            },
            {
                "id": "3",
                "partner_name": "苗文辉",
                "percent": "1.00%",
                "invest_count": "100",
                "invest_date": "-"
            }
        ]
    },
    {
        "company_name": "西藏小米科技有限责任公司",
        "company_code": "-",
        "member": [
            {
                "id": "1",
                "partner_name": "雷军",
                "title": "执行董事兼总经理"
            },
            {
                "id": "2",
                "partner_name": "黎万强",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "小米科技有限责任公司",
                "percent": "",
                "invest_count": "小米科技有限责任公司大股东股权结构>",
                "invest_date": ""
            }
        ]
    },
    {
        "company_name": "天津顺米投资有限公司",
        "company_code": "91120116300410327T",
        "member": [
            {
                "id": "1",
                "partner_name": "刘德",
                "title": "经理"
            },
            {
                "id": "2",
                "partner_name": "雷军",
                "title": "执行董事"
            },
            {
                "id": "3",
                "partner_name": "JINLINGZHANG",
                "title": "监事"
            }
        ],
        "partner": [
            {
                "id": "1",
                "partner_name": "苏州工业园区顺为科技创业投资合伙企业(有限合伙)",
                "percent": "99.00%",
                "invest_count": "9900",
                "invest_date": "2034-08-01"
            },
            {
                "id": "2",
                "partner_name": "拉萨经济技术开发区顺盈投资有限公司",
                "percent": "1.00%",
                "invest_count": "100",
                "invest_date": "2034-08-01"
            }
        ]
    }
]


def write_to_excel(json_com, json_detail, person):
    result_data = [['人员','id','公司名称','注册资本','地区','行业','状态','持股比例','统一社会信用代码', '主要人员','股东信息']]
    for com in json_com:
        data = ['-' for n in range(11)]
        data[0] = person
        data[1] = com['id']
        data[2] = com['company_name']
        data[3] = com['invest_sum']
        data[4] = com['location']
        data[5] = com['scope']
        data[6] = com['status']
        data[7] = com['invest_percent']

        for detail in json_detail:
            if detail['company_name'] == com['company_name']:
                data[8] = detail['company_code']

                data[9] = ""
                for m in detail['member']:
                    text = m['partner_name'] + "-" + m['title'] + '\n'
                    data[9] = data[9] + text

                data[10] = ""
                for p in detail['partner']:
                    text = p['partner_name'] + "-" + p['percent'] + "-" +  p['invest_count'] + '\n'
                    data[10] = data[10] + text

        result_data.append(data)

    with open(person + ".csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for l in result_data:
            writer.writerow(l)

    return result_data


result = write_to_excel(a, b, '雷军')
