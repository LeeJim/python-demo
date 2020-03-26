import json

d = open('./imgs.json', encoding='utf-8')
s = ''

for i in json.load(d):
    s += json.dumps(i)
    s += '\n'

with open('raw.json', 'w') as f:
    f.write(s)