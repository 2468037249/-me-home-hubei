from multiprocessing import Pool
import time

def show():
	for i in range(5):
		time.sleep(1)
		print('天使彦')

p = Pool() #创建一个池子，把进程装在池子里
for i in range(3): # 一次添加3个进程到池子里
	p.apply_async(show) # 添加到一个池子里，非阻塞型，3个进程同时进行，属于多任务
	#p.apply(show) # 添加到一个池子里，阻塞型，3个进程，一个添加完再添加下一个，属于单任务
	print('天使雨桐')

p.close()
p.join()
print('神圣凯莎')

