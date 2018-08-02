tudents =[]
while True:
	print("欢迎使用学生管理系统!")
	print("1:添加学生信息")
	print("2:查看学生信息")
	print("3:修改学生信息")
	print("4:删除学生信息")
	print("5:打印学生信息")
	print("6:退出学生管理系统")
	num = int(input("请选择功能:"))
	if num == 1:
		stu = {}
		name = input("请输入学生姓名:")
		age = int(input("请输入学生年龄:"))
		sex = input("请输入学生性别:")
		phone = int(input("请输入电话号码:"))
		stu["name"] = name
		stu["age"] = age
		stu["sex"] = sex
		stu["phone"] = phone
		students.append(stu)
		print("添加成功!")
		print("")
		print(students)
	elif num == 2:		
		name = input("请输入学生姓名:")
		for stu in students:
			if stu["name"] == name:
				print("正在查找中")
				print("")
				print("学生姓名：%s\n学生年龄:%d\n学生性别:%s\n电话号码:%d"%(name,age,sex,phone))
	elif num == 3:
		name = input("请输入学生姓名:")
		for stu in students:
			if stu["name"] == name:
				print("")
				print("学生姓名:%s\n学生年龄:%d\n学生性别:%s\n电话号码:%d"%(name,age,sex,phone))
				print("")
				print("1:修改姓名")
				print("2:修改年龄")
				print("3:修改性别")
				print("4:修改电话号码")
				a = int(input("请选择项目:"))
				if a == 1:
					name = input("请输入修改后的姓名:")
					stu["name"] == name
				elif a == 2:
					age = int(input("请输入修改后的年龄:"))
					stu["age"] = age
				elif a == 3:
					sex = input("请输入修改后的性别:")
					stu ["sex"] == sex
				elif a == 4:
					phone = int(input("请输入修改后的电话号码:"))
					stu["phone"] ==phone
					break
	elif num == 4:
		name = input("请输入学生姓名:")
		for stu in students:
			if stu["name"] == name:
				students.remove(stu)
				print("删除成功\n请确认")
				break
	elif num == 5:
		print("学生姓名    年龄    性别   电话号码        ")
		for sut in students:
			print(sut["name"],end = "      ")
			print(sut["age"],end = "      ")
			print(sut["sex"],end = "     ")
			print(sut["phone"],end = "   ")
			print("")
	elif num == 6:
		print("欢迎下次使用")
		break

