# -*- coding:utf8 -*-
__author__ = 'quanchimi'

import requests
from bs4 import BeautifulSoup

s=requests.session()
jwc_url = 'http://jwc.xhu.edu.cn/default6.aspx'

result = s.get(jwc_url)

soup = BeautifulSoup(result.text,"html.parser")
VIEWSTATE = soup.body.form.input['value']

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Content-Length': '447'    ,
    # 'Content-Type':'application/x-www-form-urlencoded',
    # 'Host':'jwc.xhu.edu.cn',
    # 'Origin':'http://jwc.xhu.edu.cn',
    # 'Referer':'http://jwc.xhu.edu.cn/default6.aspx',
    # 'Connection':'keep-alive',
}

data={
    '__VIEWSTATE':VIEWSTATE,
    # 'tbtns':'',
    # 'tnameXw': 'yhdl',
    # 'tbtnsXw': 'yhdl|xwxsdl',
    'txtYhm': '312012080609303',
    # 'txtXm':'',
    'txtMm': 'qq142857',
    'rblJs': '学生',
    'btnDl': '登陆'
}

xs_main_page = 'http://jwc.xhu.edu.cn/xs_main.aspx?xh=312012080609303'

login_result = s.post(jwc_url,headers=headers,data=data)
# print(login_result)
r2 = s.get(xs_main_page)
print(r2.url)

cjcx_url = 'http://jwc.xhu.edu.cn/xscjcx.aspx?xh=312012080609303'
cjcx = s.get(cjcx_url)
print(cjcx.text)

