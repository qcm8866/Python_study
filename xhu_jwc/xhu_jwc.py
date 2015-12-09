# -*- coding:utf8 -*-
import requests
from bs4 import BeautifulSoup

__author__ = 'quanchimi'
__version__ = '0.01'

xh = '312012080609303'
s = requests.session()
url = 'http://jwc.xhu.edu.cn'
jwc_url = 'http://jwc.xhu.edu.cn/default6.aspx'

result = s.get(jwc_url)

soup_login = BeautifulSoup(result.text, "lxml")
login_VIEWSTATE = soup_login.body.form.input['value']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Content-Length': '447',
    # 'Content-Type':'application/x-www-form-urlencoded',
    # 'Host':'jwc.xhu.edu.cn',
    # 'Origin':'http://jwc.xhu.edu.cn',
    # 'Referer':'http://jwc.xhu.edu.cn/default6.aspx',
    # 'Connection':'keep-alive',
}
data = {
    '__VIEWSTATE': login_VIEWSTATE,
    # 'tbtns':'',
    # 'tnameXw': 'yhdl',
    # 'tbtnsXw': 'yhdl|xwxsdl',
    'txtYhm': xh,
    # 'txtXm':'',
    'txtMm': 'qq142857',
    'rblJs': '学生',
    'btnDl': '登陆'
}

xs_main_url = 'http://jwc.xhu.edu.cn/xs_main.aspx?xh=' + str(xh)

login_result = s.post(jwc_url, headers=headers, data=data)

# print(login_result)
xs_main_page = s.get(xs_main_url)
soup_main_page = BeautifulSoup(xs_main_page.text,"lxml")
cjcx = soup_main_page.find('a',attrs={'onclick':"GetMc('成绩查询');"})
cjur = cjcx["href"]
cjur_list = cjur.split('&')
xm_list = cjur_list[1]
xm = xm_list[3:]


# main_page_VIEWSTATE = soup_main_page.body.form.input.next_sibling.next_sibling.next_sibling.next_sibling["value"]
main_page_headers = {
    'Referer': xs_main_url
}
cjcx_params = {
    'xh': xh,
    'xm': xm,
    'gnmkdm': 'N121605'
}

cjcx_url = 'http://jwc.xhu.edu.cn/xscjcx.aspx?'
cjcx_page = s.get(cjcx_url, headers=main_page_headers, params=cjcx_params)
soup_cjcx_page = BeautifulSoup(cjcx_page.text, "lxml")
cjcx_VIEWSTATE = soup_cjcx_page.body.form.input.next_sibling.next_sibling.next_sibling.next_sibling["value"]

cjcx_headers = {
    'Origin': 'http://jwc.xhu.edu.cn',
    'Referer': cjcx_page.url
}

cjcx_data = {
    '__VIEWSTATE': cjcx_VIEWSTATE,
    'btn_zg': '课程最高成绩',
}

# print(cjcx_page.url)
cjcx_result_page = s.post(cjcx_page.url, data=cjcx_data, headers=cjcx_headers)
# cjcx_result.encoding = 'gb2312'

soup_cjcx_result_page = BeautifulSoup(cjcx_result_page.text, 'html5lib')
# soup_cjcx_result.encoding = 'gb2312'

for tr in soup_cjcx_result_page.find_all('tr', attrs={'class': 'alt'}):
    print(tr)

cjcx_result= soup_cjcx_result_page.find('tr', attrs={'class': 'alt'})


# for td in cjcx_result.find_all('td'):
#     print(td)
# print(cjcx_result.td)


