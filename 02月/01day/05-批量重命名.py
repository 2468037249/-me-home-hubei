import os
dir = input("请输入文件夹:")
files = os.listdir(dir)
'''
os.chdir(dir)
print(os.getcwd())
for i in files:
	#position = i.rfind('.')
	#newname = i[0:position] + '-动漫' + i[position:]
	#print(newname)
	position = i.rfind('.')
	newname = i[:position] + '-动漫' + i[:position]
	os.rename(i,newname)
'''
for i in files:
	pos = i.rfind('.')
	newname = i[:pos]+'-动漫'+i[pos:]
	old_name = dir+'/'+i
	new_name = dir+'/'+newname
	os.rename(old_name,new_name)
