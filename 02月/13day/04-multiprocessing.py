from multiprocessing import Process
import time

def show(name):
	for i in range(10):
		time.sleep(2)
		print(name)

p = Process(target=show, args=('割草', ))
p.start()
#p.join() # 等待子进程结束后，在运行
#p.join(5) # 等待子进程运行5秒，在运行
time.sleep(2)
p.terminate()
for j in range(10):
	time.sleep(2)
	print('吃喝玩乐')


