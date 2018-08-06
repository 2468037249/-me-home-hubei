list = []
def add():
	dd = {}
	name = input("输入姓名:")
	age = int(input("输入年龄:"))
	sex = input("输入性别:")
	dd['name'] = name
	dd['age'] = age
	dd['sex'] = sex
	list.append(dd)
	savecard()
def savecard():
	f = open('cate.data','w')
	f.write(str(list))
	f.close()
	readcard()
def readcard():
	f1 = open('cate.data','r')
	content = f1.read()
	if len(content) != 0:
		list = eval(content)
		for i in list:
			for k,v in i.items():
				print(k,v)
		print(list)
	f1.close()

add()
