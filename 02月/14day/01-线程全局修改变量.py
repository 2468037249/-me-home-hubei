from threading import Thread

num = 0

def work1():
	global num
	for i in range(1000000):
		num+=1
	print('thread_1')
	print(num)

def work2():
	global num 
	for i in range(1000000):
		num+=1
	print('thread_2')
	print(num)

t1 = Thread(target=work1)
t1.start()
t2 = Thread(target=work2)
t2.start()

