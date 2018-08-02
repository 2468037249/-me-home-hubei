list = [1,2,3,4,5,7,9,15,27,38,58]
min = 0 
max = len(list)-1
count = int(input("请输入数字:"))
while True:
	center = int((min+max)/2)
	if list[center] > count:
		max = center - 1
	elif list[center] < count:
		min = center + 1
	elif list[center] == count:
		print("索引是%d"%center)
		break
