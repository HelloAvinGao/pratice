# 导入bs4模块
from bs4 import BeautifulSoup
import requests
import urllib.request
import sys  #引入模块
# r = requests.get('http://www.yy6080.cn/')
#
# html = r.text
# # 做一个美味汤
# soup = BeautifulSoup(html,'html.parser')

# url = 'http://www.yy6080.cn/'


url = sys.argv[1]

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,fromEncoding="gb18030")
print(soup.originalEncoding)

# 输出结果
print(soup.prettify())

#找到文档的title
print(soup.title)
# <title>The Dormouse's story</title>

#title的name值
print(soup.title.name)
# u'title'

#title中的字符串String
print(soup.title.string)
# u'The Dormouse's story'

#title的父亲节点的name属性
print(soup.title.parent.name)
# u'head'

print(soup.meta)

#文档的第一个找到的段落
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

#找到的p的class属性值
# print(soup.p['class'])
# u'title'

#找到a标签
print(soup.a)
# http://example.com/elsie" id="link1">Elsie

#找到所有的a标签
print(soup.find_all('a'))
# [http://example.com/elsie" id="link1">Elsie,
#  http://example.com/lacie" id="link2">Lacie,
#  http://example.com/tillie" id="link3">Tillie]

#找到id值等于3的a标签
print(soup.find(id="link3"))
# http://example.com/tillie" id="link3">Tillie

for link in soup.find_all('a'):
    if link.string == None:
        pass
    else:
        print(link.string,' : ',link.get('href'))


# print(soup.get_text())
liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
