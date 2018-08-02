list = []
def showError(msg):
		print("输入有误，请重新输入"+msg)
def add():
	stu = {}
	while True:
		name = input("请输入学生姓名:")
		if len(name) > 1 and len(name) < 5:
			stu["name"] = name
			break
		else:
			showError("姓名在2字到4字之间(包含4字)")
	while True:
		age = input("请输入学生年龄:")
		if age.isdigit():
			age = int(age)
		if age > 1 and age < 150:
			stu["age"] = age
			break
		else:
			showError("年龄在1到150之间")
	sex = input("请输入学生性别:")

	phone = int(input("请输入监护人电话:"))
	mz = input("请输入民族:")
	stu["name"] = name
	stu["age"] = age
	stu["sex"] = sex
	stu["phone"] = phone
	stu["mz"] = mz
	list.append(stu)
	print("添加成功")
	print("")
	print(list)
def find():
	find_name = input("请输入学生姓名:")
	for stu in list:
		if stu["name"] == find_name:
			print("正在查找中")
			print("-"*40)
			print("姓名:%s\n年龄:%d\n性别:%s\n电话:%d\n民族:%s"%(stu["name"],stu["age"],stu["sex"],stu["phone"],stu["mz"]))
			print("-"*40)
			break
		else:
			print("查无此人")

def deal():
	find_name = input("请输入学生姓名:")
	for stu in list:
		if stu["name"] == find_name:
			print("-"*40)
			print("1:修改姓名")
			print("2:修改年龄")
			print("3:修改性别")
			print("4:修改电话号码")
			print("5:修改民族")
			print("0:返回上级菜单")
			a = int(input("请选择功能:"))
			if a == 1:
				name = input("请输入姓名:")
				stu["name"] = name
			elif a == 2:
				age = int(input("请输入年龄:"))
				stu["age"] = age
			elif a == 3:
				sex = input("请输入性别:")
				stu["sex"] = sex
			elif a == 4:
				phone = int(input("请输入电话号码:"))
				stu["phone"] = phone
			elif a == 5:
				mz = input("请输入民族:")
				stu["mz"] = mz
			elif a == 0:
				print_deng()
		print("修改成功")
def delete():
	print("姓名     年龄     性别     电话号码     民族     ")
	for stu in list:
		print(stu["name"],end = "    ")
		print(stu["age"],end = "    ")
		print(stu["sex"],end = "    ")
		print(stu["phone"],end = "    ")
		print(stu["mz"],end = "    ")
		print("")
def print_list():
	name = input("请输入姓名:")

	for stu in list:
		if stu["name"] == name:
			list.remove(stu)
			print("删除成功")
def print_deng():
	print("欢迎使用学生管理系统".center(30," "))
	while True:
		print("1:添加学生信息")
		print("2:查看学生信息")
		print("3:修改学生信息")
		print("4:打印学生信息")
		print("5:删除学生信息")
		print("6:退出学生管理系统")
		input_info()
def input_info():
	num = int(input("请选择功能:"))
	if num == 1:
		add()
	elif num == 2:
		find()
	elif num == 3:
		deal()
	elif num == 4:
		delete()
	elif num == 5:
		print_list()
	elif num == 6:
		print("欢迎下次使用")
	 	#break
print_deng()
