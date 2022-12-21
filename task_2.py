from socket import *
def poisk(data):
    f=open('gruppa.txt', 'r+', encoding='utf-8')
    a=list(f)
    name=None
    if data.encode('utf-8')==b'\n':
        name='Вы не ввели фамилию\n'
    else:
        for i in range(len(a)):
            if a[i].find(data)!=-1:
                name = 'Привет, '+a[i].split()[0]+'\n'
        if name==None:
            name='Error\n'
    return name
    f.close()
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 12000))
while True:
    data, adres = s.recvfrom(1024)
    data=data.decode('utf-8')
    otvet=poisk(data).encode('utf-8') #дeкодирование текста
    s.sendto(otvet, adres) # отправка ответа клиенту
