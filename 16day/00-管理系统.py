list = []
def pd(): # 账号
	while True:
		ac = input("请输入账号:")
		pw = input("请输入密码:")
		if ac == "dirtily" and pw == "pc12345":
			print("登录成功")
			print("-"*40)
			print_xianshi()			
			break
		else :
			print("输入错误，请检查账号和密码")
def app(): # 添加
	pass
def find(): # 查找
	pass
def deal(): # 修改
	pass
def delete(): # 删除
	pass
def print_dayin(): # 打印
	pass
def print_xianshi(): # 显示功能
	print("欢迎使用管理系统".center(30," "))
	print("0:退出系统")
	print("1:添加信息")
	print("2:查找信息")
	print("3:修改信息")
	print("4:删除信息")
	print("5:打印信息")
	print_info()

def print_info(): # 选择功能
	name = int(input("请选择功能:")) 
	if name == 1:
		app()
	elif name == 2:
		find()
	elif name == 3:
		deal()
	elif name == 4:
		delete()
	elif name == 5:
		print_dayin()
	elif name == 0:
		print("欢迎下次使用本系统")

pd()

