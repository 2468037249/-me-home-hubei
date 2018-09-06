from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.sendto('你是老王'.encode('gb2312'),('192.168.56.1',8080))
s.close()


