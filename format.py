import json

d = open('./imgs.json', encoding='utf-8')
s = ''
has_watermark = set()
has_watermark.add('789763565')
for i in json.load(d):
    ratio = float(i['height']) / float(i['width'])
    i['ratio'] = round(ratio, 1)
    cond = i['answerId'] not in has_watermark
    if ratio > 1 and ratio < 3 and cond:
        s += json.dumps(i)
        s += '\n'
    else:
        print(i['src'])

with open('raw.json', 'w') as f:
    f.write(s)