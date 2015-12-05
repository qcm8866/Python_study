# -*- coding:utf8 -*-
__author__ = 'quanchimi'

import requests

headers ={
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
    ' YB_SSID' : '2355e49a0c70b1d1c29b714c7f8e2db8',
    'yiban_user_token' : 'd2f8ff3fbfc127b3c57ad618df72d74b',

}

ur1 = 'http://www.yiban.cn/ajax/group/getMyManageForVote'
s=requests.post(ur1)
cookies =s.cookies
print(s)

ur2 = 'http://www.yiban.cn'
r2= requests.get(ur2,cookies=cookies)
