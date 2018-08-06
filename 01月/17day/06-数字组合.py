'''
2、有1 2 3 4
用这个数字 能组成几个不重复的三位数
'''
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i!=j and j!=k and k!=i:
				print(i,j,k)




