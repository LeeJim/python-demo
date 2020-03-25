from urllib.parse import urljoin

import re
import requests
import json

from bs4 import BeautifulSoup

def main():
    d = open('./data.json', encoding='utf-8')
    
    headers = {'user-agent': 'Baiduspider'}
    base_url = 'https://www.zhihu.com/'
    count = 0
    for i in json.load(d):
        seed_url = urljoin(base_url, 'question/'+ i['questionId'] + '/answer/' + i['id'])
        resp = requests.get(seed_url,
                            headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        for img in soup.find_all('img'):
            if img.has_attr('data-original'):
                count+=1
                print(img['data-original'])
                print(img['data-rawheight'])
                print(img['data-rawwidth'])

    print('total: %d', %(count))
if __name__ == '__main__':
    main()