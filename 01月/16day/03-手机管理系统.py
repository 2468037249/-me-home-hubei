list = []

def showError():
	print("输入错误请重新输入")

def isNum(num):
	if num.isdigit():
		return True
	else:
		return False

def deng():
	while True:
		print("-"*50)
		ac = input("请输入账号:")
		pd = input("请输入密码:")
		if ac == "luohao" and pd == "123..":
			print("登陆成功")
			print("")
			print("-"*45)
			print("欢迎使用本系统".center(30," "))
			print_xian()
			break
		else:
			print("请检查账号密码")
def add(): # 添加 
	print("")
	phone = {}
	while True:
		name = input("请输入品牌:")
		if len(name) >= 2:
			phone["name"] = name
			break
		else:
			showError()
	while True:
		numder = input("请输入数量:")
		if isNum(numder) :
			numder = int(numder)
			phone["numder"] = numder
			break
		else:
			showError()
	price = float(input("请输入价格:"))
	phone["price"] = price
	list.append(phone)
	print("")
def find(): # 查看
	name = input("请输入品牌:")
	for phone in list:
		if phone["name"] == name:
			print("手机品牌:%s\n数量:%d\n单价:%.02f\n"%(phone["name"],phone ["numder"],phone["price"]))
			break
def chace(): # 修改
	name = input("请输入品牌:")
	for phone in list:
		if phone["name"] == name:
			print("")
			print("1:修改数量")
			print("2:修改价格")
			print("0:返回上级菜单")
			a = input("请选择功能:")
			if isNum(a):
				a = int(a)
			else:
				print("输入有误")
				continue
			if a == 1:
				while True:
					numder = input("请输入数量:")
					if isNum(numder):
						numder = int(numder)
						phone["numder"] = numder
						break
					else:
						showError()
			elif a == 2:
					price = float(input("请输入价格:"))
					phone["price"] = price
			elif a == 0:
				print_xian()
			else:
				print("无此功能,请从新选择")
		else:
			showError()
def delete(): # 删除
	name = input("请输入品牌:")
	for phone in list:
		if phone["name"] == name:
			list.remove(phone)
			print("删除成功")
			break
def print_ad(): # 打印
	print("手机品牌      数量      价格")
	for phone in list:
		print("%s          %d       %d"%(phone["name"],phone["numder"],phone["price"]))
def print_xian(): # 功能
	while True:
		print("1:添加")
		print("2:查看")
		print("3:修改")
		print("4:删除")
		print("5:打印")
		print("0:退出")
		print("")
		input_info()
def input_info(): # 选择功能
	num = input("请选择功能:")
	if isNum(num):
		num = int(num)
		if num ==1:
			add()
		elif num == 2:
			find()
		elif num == 3:
			chace()
		elif num == 4:
			delete()
		elif num == 5:
			print_ad()
		elif num == 0:
			print("欢迎下次使用本系统") 
			exit()
	
		else :
			print("没有此功能")
			print("")
deng()







