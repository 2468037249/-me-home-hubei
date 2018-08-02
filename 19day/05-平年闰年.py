age = int(input("请输入年份:"))

if age % 4 == 0 and age % 100 != 0:
	print("%d是闰年"%age)
elif age % 400 == 0:
	print("%d是闰年"%age)
else:
	print("%d是平年"%age)
