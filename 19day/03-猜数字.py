import random
pc = random.randint(1,100)
for i in range(1,11):
	num = int(input("1:100之间\n请输入数字:"))
	if num > pc :
		print("数字有点大，需要小点")
	elif num < pc:
		print("数字有点小，需要大点")
	else:
		print("恭喜玩家胜利")
		break
print("一共猜了%d次"%i)
		
