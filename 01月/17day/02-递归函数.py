def test(num):

	if  num == 1:
		return num
	else :
		return num*test(num-1)
'''
ret = test(5)
print(ret)
'''
def test1(num):
	if num == 1:
		return num
	else :
		return num + test1(num-1)
'''
ret = test1(10)
print(ret)
'''
def test2(num):
	if num == 1:
		return num
	else :
		return num/test2(num-1)

ret = test2(18)
print(ret)
