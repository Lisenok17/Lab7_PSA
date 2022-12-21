import http.client
conn = http.client.HTTPSConnection('beda.pnzgu.ru')
print(conn)
conn.request("GET", "/anatoly/")
r=conn.getresponse()
# статус ответа
print('Proto : ', r.version)
print('Code :', r.status)
print('Status :', r.reason)
# заголовки ответа
print('---------- HEADERS ----------')
print(r.headers)
# тело ответа
print('----------- BODY ------------')
print(r.read().decode())
conn.close()
