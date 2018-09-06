name = input('输入文件名(要有后缀名)')
f = open(name,'r')
content = f.read()

#position = name.rfind(".")
#newname = name[0:position] + '备份' + name[position:]

pos = name.rfind('.')
dian = name.find('-')
newname = name[dian+1:pos] + '备份.txt'


f1 = open(newname,'w')
while True:
	content = f.read(1024)
	f1.write(content)
	if len(content) == 0:
		break
	f1.write(content)

f.close()
f1.close()
