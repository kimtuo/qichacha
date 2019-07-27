from qichacha import Qichacha
import tkinter, os, json, xlwt

# 创建一个主窗口
win = tkinter.Tk()
# 设置标题
win.title("企查查")
# 设置窗口大小和位置
win.geometry("500x500+250+150")
# 设置一个变量，用来接收输入控件得内容
keyword = tkinter.Variable()
v_dir = tkinter.Variable()
result_label = tkinter.Variable()


v_dir.set("D:\\Qichacha\\")

label_dir = tkinter.Label(win,text='输出文件夹')
label_dir.place(x=10, y=100)
excel_dir = tkinter.Entry(win, textvariable=v_dir)
excel_dir.place(x=100, y=100)

# 输入框控件
entry_dir = tkinter.Label(win,text='法人名字：')
entry = tkinter.Entry(win, textvariable=keyword)

entry_dir.place(x=30, y=200)
entry.place(x=80, y=200)

result_label.set("")
label_result = tkinter.Label(win,text=result_label)

# 设置输入框内默认内容
keyword.set("陀金生")
print(keyword.get())


def write_excel_xls(sheet_name, value, file_name, dir):
    path = dir + file_name + '.xls'
    print(path)
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    sheet.write(0, 0, "法人")
    sheet.write(0, 1, "注册资金")
    sheet.write(0, 2, "注册时间")
    sheet.write(0, 3, "行业")
    sheet.write(0, 4, "公司名称")
    sheet.write(0, 5, "省份")
    sheet.write(0, 6, "主要人员")
    sheet.write(0, 7, "股东信息")
    sheet.write(0, 8, "社会统一信用代码")
    sheet.write(0, 9, "经营状态")
    sheet.write(0, 10, "注销时间")
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i + 1, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

def format_to_excel(data, person):
    excel_data = []
    for d in data:
        excel_list = [0,0,0,0,0,0,0,0,0,0,0]
        excel_list[0] = person
        excel_list[1] = d["invest_sum"]
        excel_list[2] = d["establish_date"]
        excel_list[3] = d["scope"]
        excel_list[4] = d["company_name"]
        excel_list[5] = d["location"]
        members = ""
        for m in d["member"]:
            members = members + "\n" + m["partner_name"] + "-" +  m["title"] + ";  "
        excel_list[6] = members

        partners = ""

        for m in d["partner"]:
            partners = partners + "\n" + m["partner_name"] + "-" + m["percent"] + "-" + m["invest_count"] + "万元;  "
        excel_list[7] = partners

        excel_list[8] = d["company_code"]
        excel_list[9] = d["status"]
        excel_list[10] = "-"

        excel_data.append(excel_list)

    return excel_data

# 设置按钮提交
def search():
    result_label.set("开始查询...")
    if not os.path.exists(v_dir.get()):
        os.mkdir(v_dir.get())
    person = entry.get()
    qichacha = Qichacha()
    qichacha.keywords = person
    c_list = qichacha.find_company_by_person(person)
    result = qichacha.get_company_info_from_json_list(c_list)

    excel_data = format_to_excel(result, person)
    write_excel_xls(person, excel_data, person, v_dir.get())

    qichacha.browser.quit()

    print(json.dumps(result, indent=4, ensure_ascii=False))
    result_label.set("查询完毕")
    return result

button = tkinter.Button(win, text="提交", command=search)
button.place(x=50, y=230)


# 启动主窗口
win.mainloop()
