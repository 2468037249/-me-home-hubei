def test(a,b,*args,c = 12,**kwargs):
	print(a)
	print(b)
	print(args)
	print(c)
	print(kwargs)

t = (3,4,5) #拆包
d = {"s":12,"j":32} #同上
test(1,6,*t,c=40,**d)
