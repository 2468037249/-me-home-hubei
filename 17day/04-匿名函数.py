'''
fun = lambda x,y:x+y
print(fun(1,2))
'''
def test(x,y,z):
	ret = z(x,y)
	return ret
ret = test(1,3,lambda x,y:x+y)
print(ret)
