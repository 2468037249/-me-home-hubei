from socket import *
import time

s = socket(AF_INET, SOCK_DGRAM)

while True:

	name = input(':')

	s.sendto(name.encode('gb2312'), ('192.168.56.1',8080))
	time.sleep(3)

#sendData = rew_input("请输入要发送的数据")

#udpSocket.sendto(senData, sendAddr)
while True:
	rets = s.recvfrom(1024)
	print(rets)
	print(rets[0].decode('gb2312'))
	print(rets[1][0])
	print(rets[1][1])


s.close()


