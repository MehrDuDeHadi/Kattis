import requests
import re
from lxml import etree
import lxml.html
import pymongo
mnews=[{'موضوعات داغ روز':''},
       {'خبرهای بیشتر':''},
       {'مطالب منتخب':''}
]
html = requests.get('https://per.euronews.com/')
doc = lxml.html.fromstring(html.content)
article = doc.xpath('/html/body/main/div/div[1]/article/div[2]/h2/a')
article1=doc.xpath('/html/body/main/div/div[2]/article[*]/div[2]/h2/a')
for i in article:
    mnews[0]['موضوعات داغ روز'] += i.text.strip()
for i in article1:
    mnews[0]['موضوعات داغ روز'] += i.text.strip()
article2=doc.xpath('/html/body/main/section[6]/div/div/article[*]/div[2]/h3/a')
for i in article2:
   mnews[1]['خبرهای بیشتر'] += i.text.strip()
article3=doc.xpath('/html/body/main/section[7]/div/div/article[*]/div[2]/h3/a')
for i in article3:
    mnews[2]['مطالب منتخب'] += i.text.strip()
mclient = pymongo.MongoClient("mongodb://localhost:27017/")
mdb = mclient["euronews"]
mcol = mdb["titles"]
print(mnews)
x = mcol.insert_many(mnews)