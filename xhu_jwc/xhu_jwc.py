# -*- coding:utf8 -*-
__author__ = 'quanchimi'

import requests
from bs4 import BeautifulSoup

s=requests.session()
jwc_url = 'http://jwc.xhu.edu.cn/default6.aspx'

result = s.get(jwc_url)

soup_login = BeautifulSoup(result.text,"html.parser")
login_VIEWSTATE = soup_login.body.form.input['value']

xh='312012080609303'
headers ={
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

data={
    '__VIEWSTATE':login_VIEWSTATE,
    # 'tbtns':'',
    # 'tnameXw': 'yhdl',
    # 'tbtnsXw': 'yhdl|xwxsdl',
    'txtYhm': xh,
    # 'txtXm':'',
    'txtMm': 'qq142857',
    'rblJs': '学生',
    'btnDl': '登陆'
}

xs_main_url = 'http://jwc.xhu.edu.cn/xs_main.aspx?xh='+str(xh)

login_result = s.post(jwc_url,headers=headers,data=data)

# print(login_result)
xs_main_page = s.get(xs_main_url)
# print(xs_main_page.text)
cjcx_headers={
    'Referer': 'http://jwc.xhu.edu.cn/xs_main.aspx?xh=312012080609303'
}
cjcx_url = 'http://jwc.xhu.edu.cn/xscjcx.aspx?xh=312012080609303&xm=%C8%A8%B3%DB%F4%CD&gnmkdm=N121605'
cjcx_page =s.get(cjcx_url,headers=cjcx_headers)



# soup_main_page = BeautifulSoup(xs_main_page.text,"lxml")
# main_page_VIEWSTATE = soup_main_page.body.form.input.next_sibling.next_sibling.next_sibling.next_sibling["value"]
# main_data={
#     '__VIEWSTATE':main_page_VIEWSTATE,
#     'btn_zg':'课程最高成绩'
# }


# cjcx_url = 'http://jwc.xhu.edu.cn/xscjcx.aspx?xh=312012080609303&xm=%C8%A8%B3%DB%F4%CD&gnmkdm=N121605'
# cjcx_post.encoding='utf-8'
# print(cjcx_post.text)
# # cjcx = s.get(cjcx_url,data=cjcx_data)
# # print(cjcx)
# # print(cjcx.url)
# # print(cjcx.text)
# # # cjcx_url = 'http://jwc.xhu.edu.cn/xscjcx.aspx?xh=312012080609303&xm=%C8%A8%B3%DB%F4%CD&gnmkdm=N121605'
# #
# # cjcx = s.get(cjcx_url,params =cjcx_data)
# # print(cjcx.text)
# # print(cjcx.url)
# # print(r2.text)
