from socket import *
def poisk(data):
    f=open('gruppa.txt', 'r+', encoding='utf-8')
    a=list(f)
    name=None
    if data.encode('utf-8')==b'\n':
        name='Вы не ввели фамилию\n'
    else:
        for i in range(len(a)):
            if a[i].find(data)!=-1: #find это поиск
                name = 'Привет, '+a[i].split()[0]+'\n' #split - разбиение
        if name==None:
            name='ERROR\n'
    return name
    f.close()
try:
    s = socket(AF_INET, SOCK_STREAM) #веб-протокол 
    s.bind(('127.0.0.1', 3333)) #назначение ip адреса и порта
    while True:
        s.listen() #показывает количество запросов и ставит их в ожидание если их число больше чем в скобках они сбрасываются
        client_socket, adres = s.accept() #принимает запрос и разделяет его на клиента и адрес клиента
        # программа фиксируется на этом моменте и ждёт подключение клиента
        otvet='Напишите свою фамилию\n'.encode('utf-8') #дeкодирование текста
        client_socket.send(otvet) # отправка ответа клиенту
        data = client_socket.recv(1024).decode('utf-8') #получение содержимого запроса и декодировка из байтового вида
        print(data.encode('utf-8'))
        otvet=poisk(data).encode('utf-8') #дeкодирование текста
        client_socket.send(otvet) # отправка ответа клиенту
        client_socket.shutdown(SHUT_WR) #закрытие соединения с данным клиентом после отправления ему ответа
except KeyboartInterrupt:  
    s.close()
