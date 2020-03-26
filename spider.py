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
    data = json.load(d)
    def sortByVote(i):
        return i['upvoteNum']
    data.sort(key=sortByVote, reverse=True)

    # 去重
    def unique(items, key=None):
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)
    data = list(unique(data, key=lambda d: d['id']))

    imgList = []
    print('total: %d' %(len(data)))
    for i in data:
        seed_url = urljoin(base_url, 'question/'+ i['questionId'] + '/answer/' + i['id'])
        resp = requests.get(seed_url,
                            headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        for img in soup.find_all('img', class_="lazy"): # 过滤noscript的部分
            if img.has_attr('data-original'):
                imgList.append({
                    'answerId': i['id'],
                    'width': img['data-rawwidth'],
                    'height': img['data-rawheight'],
                    'src': img['data-original']
                })
        count += 1
        print('finish %d/%d.' %(count, len(data)))
    with open('./imgs.json', 'w') as f:
        f.write(json.dumps(imgList))
    print('all finish')
if __name__ == '__main__':
    main()
