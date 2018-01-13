import requests
from bs4 import BeautifulSoup
import re


req = requests.get('https://www.clien.net/service/group/allreview?&od=T31&po=0')
#print(req)


html = req.text
#print(html)


soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'a.list_subject'
    )

f= open("memo.txt", 'w+', encoding='utf8')
f.write("")
f.close

for title in my_titles[1:]:
    
    a = title.select("span:nth-of-type(2)")
    cooltext1 = re.sub('<.+?>', '', str(a), 0, re.I|re.S)
    
    b = title.get('href')
    c = "https://www.clien.net"

    req2 = requests.get(c + str(b))
    html2 = req2.text
    soup2 = BeautifulSoup(html2, 'html.parser')
    my_titles2 = soup2.select(
        'article > div'
        )
    cooltext2 = re.sub('<.+?>', '', str(my_titles2), 0, re.I|re.S) 

    #print(my_titles2)

    f= open('memo.txt', 'a', encoding='utf8')
    f.write(cooltext1)
    f.write('\n')
    f.write(c + str(b))
    f.write('\n')
    f.write(cooltext2)
    f.write('\n')
    f.write('\n')
    f.close
    

  
