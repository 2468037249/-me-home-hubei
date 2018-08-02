import random
for i in range(10):
	pc = random.randint(1,3)
	player = int(input("1:石头2:剪刀3:布\n请输入序号:"))
	if ((player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1)):
		print("玩家 win")
		break
	elif player == pc:
		print("平局")
	else:
		print("电脑 win")
	
