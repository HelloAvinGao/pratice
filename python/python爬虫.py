# import requests

# header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

# def baidu(company):
#     url = 'https://www.baidu.com/s?tn=news$rtt=1&bsst=1&c1=2&wd=' + company
#     res = requests.get(url,headers=header).text
#     print(res)
import requests
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
print(strhtml.text)