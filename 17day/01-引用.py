def test(a): # 形参
	a+=a
	print(a)
'''
d = [1,3] # 实参
test(d)
print(d)
'''

def tast(a):
	a=a+a
	print(a)
'''
w = [3,4]
tast(w)
print(w)
'''

def test1(a):
	a=a+a
	print(a)

w = (1,3)
test1(w)
print(w)




#列表，元组 可以 字典报错
 #a=a+a 对于可变类型数据来说 先算右边 给出一个新的变量

 #a+=a  对于可变类型数据来说 a 是存在的引用 直接对值进行修改的
