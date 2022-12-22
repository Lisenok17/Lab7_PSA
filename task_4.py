import http.client
def zagruzka(f):
    conn.request("GET", d+f)
    r=conn.getresponse()
    n=r.read()
    f=open('1.jpg', 'bw')
    f.write(n)                   #функция загрузки изображения  
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    global f
                    f=attr[1]
                    return f
parser = MyParser()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
d='/anatoly/'
conn.request('GET', d)
r = conn.getresponse()
parser.feed(r.read().decode())
parser.close()

zagruzka(f)
