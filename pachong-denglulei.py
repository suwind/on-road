import urllib.request
import urllib.parse
import http.cookiejar
# setting headers
url='https://www.zhihu.com/#signin'
user_agent='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
values={'username':'13811917534','password':'412131'}
headers={'User-Agent':user_agent,'Referer':'https://www.zhihu.com/'}
data=urllib.parse.urlencode(values)
request=urllib.request.Request(url,data,headers)
reponse=urllib.request.urlopen(request,timeout=10) #setting timoout
page=reponse.read()
print (page)

# setting proxy
enable_proxy=True
proxy_handler=urllib.request.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler=urllib.request.ProxyHandler({})
if enable_proxy:
    opener=urllib.request.build_opener(proxy_handler)
else:
    opener=urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)
# urllib.request.install_opener是全局的opener,可以使用opener.open
# class RedirectHandler(urllib2.HTTPRedirectHandler):
#     def http_error_301(self, req, fp, code, msg, headers):
#         print
#         "301"
#         pass
#
#     def http_error_302(self, req, fp, code, msg, headers):
#         print
#         "303"
#         pass
#
#
# opener = urllib2.build_opener(RedirectHandler)
# opener.open('http://rrurl.cn/b1UZuP')

#setting except
url= "http://blog.csdn.net/cqcre"
request=urllib.request.Request(url)
try:
    urllib.request.urlopen(request)
except urllib.request.HTTPError as e:
    print(e.code,e.reason)

#变量保存cookie
cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
reponse=opener.open('http://www.baidu.com')
for item in cookie:
    print('Name='+item.name)
    print('Value='+item.name)

#file保存cookie
filename='C:\Program Files (x86)\pyhon\\test1\cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
reponse=opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

 #模拟登陆withcookie
filename='C:\Program Files (x86)\pyhon\\test1\cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
postdata=urllib.parse.urlencode({
    'username':'dongcui@ixianlai.com',
    'password':'qwert1234'
}).encode("utf-8")
opener.open('https://aso100.com/account/signin',postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
url1='https://aso100.com/app/downloadEstimate/appid/1251313037/country/cn'
result=opener.open(url1)
print(result.read())

# Debug Log
# 使用 urllib2 时，可以通过下面的方法把 debug Log 打开，这样收发包的内容就会在屏幕上打印出来，方便调试，有时可以省去抓包的工作

httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httpHandler, httpsHandler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.google.com')

# 用firefox+httpfox插件来看看自己到底发送了些什么包

import socket
import types

hostname=socket.gethostname()
local_ip=socket.gethostbyname(hostname)
ip_lists=socket.gethostbyname_ex(hostname)

import os

a=os.walk('E:\工作\文档')
for i in a:
    print(i)

file=open('E:\学习\python-1\\test\jilu.txt','w+',encoding='utf-8')
file.write(result)