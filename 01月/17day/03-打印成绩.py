st = []
def add():
	for i in range(3):
		l = []
		for j in range(3):
			grade = float(input('请输入成绩'))
			l.append(grade)
		list.append(l)
	print(list)

maxgrade = 0
mp = 0
def mmax():
	global maxgrade
	global mp
	for p,i in enumerate(list): # 查看索引
		if sum(i) > maxgrade: # 最大值
			maxgrade = sum(i)
			mp = p
	print(maxgrade)
	print(mp)
	print('平均分%.02f'%(maxgrade/3))
	print(list[mp][0],list[mp][1],list[mp][2])

add()
mmax()

