# 导入模块
import requests
from bs4 import BeautifulSoup
import os
import re
# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
# 获取网页源码
def get_html(url):
    res = requests.get(url, headers=headers)
    return res.text
# 保存数据
def save_data(title, concent):
    path = '黄泉逆行'
    if not os.path.exists(path):
        os.mkdir(path)
    with open(f'{path}/{title}.txt', 'w', encoding='utf-8') as f:
        f.write(concent)
    print(f'{title}章节爬取成功--------------------------------------')
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')

    tag_div = soup.find('div', class_='listmain')
    tag_dd = tag_div.find_all('dd')
    for tag in tag_dd:
        tag_a = tag.find('a')
        title = tag_a.string
        if title == '<<---展开全部章节--->>':
            continue
        title = re.sub(r'[?*:"\/|]', '', title)
        href = 'https://www.bq03.cc' + tag_a.get('href')
        html = get_html(href)
        soup1 = BeautifulSoup(html, 'lxml')
        tag_div1 = soup1.find('div', id='chaptercontent')
        data = list(tag_div1.stripped_strings)
        concent = '\n   '.join(data)
        save_data(title, concent)
def main():
    url = 'https://www.bq03.cc/read/174553/'
    html = get_html(url)
    parse_html(html)
main()
