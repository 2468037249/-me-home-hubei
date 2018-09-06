from threading import Thread
from socket import *

s = socket(AF_INET,SOCK_DGRAM)
ip = input('请输入接收IP:')
port = int(input('请输入接收端口:'))
s.bind(("", 1356))
def send():
	while True:
		msg = input('请输入发送内容:')
		s.sendto(msg.encode('gb2312'), (ip, port))

def inst():
	while True:
		nmg = s.recvfrom(1024)
		print('\r收到消息:%s'%nmg[0].decode('gb2312'))

t1 = Thread(target=send)
t2 = Thread(target=inst)
t1.start()
t2.start()
t1.join()
t2.join()
s.close()
