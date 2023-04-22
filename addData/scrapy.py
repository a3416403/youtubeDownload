import requests
from bs4 import BeautifulSoup
import random
import time
from fake_useragent import UserAgent

# 定义目标网页链接
url = 'https://www.shubaow.net/156_156994/'
ua = UserAgent()
headers = {'User-Agent': ua.random}
# 获取网页内容
response = requests.get(url, headers=headers)
html = response.content

# 解析页面内容
soup = BeautifulSoup(html, 'html.parser')
list_div = soup.find('div', id='list')
link_list = []

# 获取链接列表
for link in list_div.find_all('a'):
    link_list.append('https://www.shubaow.net'+link.get('href'))
del link_list[:9]
# 遍历链接列表，抓取内容
content = ''
for link in link_list:
    # 获取链接页面内容
    response = requests.get(link, headers=headers)
    html = response.content
    print(link)
    # 解析页面内容，提取需要的文本信息
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', id='content')
    content += content_div.text.strip()

    # 每次抓取之后暂停一定的时间，模拟浏览行为
    time.sleep(random.randint(1, 3))

# 将提取出的文本保存到文件中
with open('./反正我是超能力者.txt', 'w', encoding='utf-8') as f:
    f.write(content)