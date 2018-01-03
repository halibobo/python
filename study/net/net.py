
import requests
from bs4 import BeautifulSoup
import re

def getCrapInfo(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    headers = {'User-Agent': user_agent}
    session = requests.session()
    page = session.get(url, headers=headers)
    soup = BeautifulSoup(page.text,'html.parser')#以html的方式解析页面，返回一个soup对象
    print(soup)
    community_div = soup.find_all('a', attrs={'name':'selectDetail', 'title':re.compile(".*")})
    for a in community_div:
        print(a.string)
getCrapInfo('http://sh.lianjia.com/xiaoqu/')
