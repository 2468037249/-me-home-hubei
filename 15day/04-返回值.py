def maichide(money):
	latiao = 3
	mian = 2
	kele = 6
	yu = money-(latiao+mian+kele)
	return yu,"辣条","方便面","可乐"

yu,latiao,mian,kele = maichide(15)
print(yu,latiao,mian,kele)
