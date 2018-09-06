from multiprocessing import Process
import time

class Show(Process):
	def __init__(self):
		super().__init__()
	
	def run(self):
		for i in range(10):
			time.sleep(1)
			print('彦')

class Show1(Process):
	def __init__(self):
		super().__init__()
	def run(self):
		for i in range(10):
			time.sleep(1)
			print('冷')

p = Show()
p1 = Show1()
p.start()
p1.start()
p.join(3)

print('凯莎')
