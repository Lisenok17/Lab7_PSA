import http.client
def zagruzka(f,i):
    conn.request("GET", d+f)
    r=conn.getresponse()
    n=r.read()
    f=open(i+'.jpg', 'bw')
    f.write(n)                   #функция загрузки изображения  
from html.parser import HTMLParser
class MyParser_str(HTMLParser):
    global a
    a=[]
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    a.append(attr[1])
            return a                  # класс ищет все возможные ссылки для переходов
class MyParser_foto(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            global s
            for attr in attrs:
                if attr[0] == 'src':
                    s=(attr[1])
            return s                        # класс ищет все изображения по ссылкам
        else:
            s=None
            return s
parser1 = MyParser_str()
conn = http.client.HTTPSConnection("beda.pnzgu.ru")
d='/anatoly/'
conn.request('GET', d)
r = conn.getresponse()
parser1.feed(r.read().decode())
parser1.close()
for i in range(len(a)):               # переходим по ссылке и передаём информацию о ней в парсер
    parser2 = MyParser_foto()
    conn.request('GET', d+a[i])
    t = conn.getresponse()
    parser2.feed(t.read().decode())
    parser2.close()
    if s!=None:
        zagruzka(s,str(i+2))        # загружаем изображения
