'''
def a():
	for i in range(1,101):
		if i % 2 == 0 :
			print("我是偶数%d"%i,end = "     ")
			print("")
		else:
			print("我是奇数%d"%i,end = "     ")
a()
'''
def showsum(end):#声明函数  end是一个形参
	sum = 0
	for i in range(1,101):
		sum+=1
	print(sum)

start = int(input("请输入起始值:"))
num = int(input("请输入终止值:"))

showsum(start,num) #实参 

