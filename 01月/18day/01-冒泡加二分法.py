list = [3,70,45,82,16,36,55,23,99,65]

for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] >list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)
