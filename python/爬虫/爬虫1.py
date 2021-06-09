import requests
import re

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

# findlink = re.compile(r'<a href="https://edu.csdn.net/course/detail/(\d*?)">')
findLink = re.compile(r'https://edu.csdn.net/course/detail/\d*')
findImgLink = re.compile(r'https://img-bss.csdnimg.cn/\d*.jpg')
findContent = re.compile(r'<p class="item_content" data-v-0a19579e>(\s*?.*?\s*?)</p>')
findTitle = re.compile(r'<span data-v-0a19579e>(\s*?.*?\s*?)</span>')

def baidu(pageNum):
    url = 'https://edu.csdn.net/course?cat1=280&channelType=2&cat2=355&page=' + pageNum + '&sort=1' #排序sort后可以改为1，2，3
    res = requests.get(url,headers=header).text
    courselink = re.findall(findLink,str(res))
    imgLink = re.findall(findImgLink, str(res))
    contentLink = re.findall(findContent, str(res))
    titleLink = re.findall(findTitle, str(res))
    print(titleLink)

baidu('2')

