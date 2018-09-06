from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 1234))
s.listen(5)

s1.info = s.accept()
print('有新链接了')

print(s1.recv(1024).decode('gb2312'))
s1.send('呵呵哈'.encode('gb2312'))


s1.close()
s.close()
