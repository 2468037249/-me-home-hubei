name = input('输入文件名(要有后缀名)')
f = open(name,'r')
content = f.read()

#position = name.rfind(".")
#newname = name[0:position] + '备份' + name[position:]

dian = name.rfind('.')
pos = name.find('-')
newname = name[pos+1:dian] + '备份.txt'


ff = open(newname,'w')
ff.write(content)

f.close()
ff.close()
