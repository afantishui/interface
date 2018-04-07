# -*- coding: utf-8 -*-
'''
	时期：2018-3-16
	文件操作 增 删 读 写
'''
import os
class file_base():

	#检查文件是否存在
	def check_file(self,filepath):
		if not os.path.isfile(filepath):
			print('文件不存在')
			return False 
		else:
			print('文件存在')
			return True

	# 新建文件
	def mkdir_file(self,filepath):
		if not os.path.isfile(filepath):
			f = open(filepath,'w+')
			f.close()
			print('创建文件成功')
			return True
		else:
			print('文件不存在')
			return False 

	# 删除文件
	def remove_file(self,filepath):
		if not os.path.isfile(filepath):
			os.remove(filepath)
			print('删除文件成功')
		else:
			print('文件不存在')

	# 读文件
	def read_txt(self,filepath):
		pass

	# 写文件
	def write_txt(self,filepath,msg):
		with open(filepath,'w')as f:
			f.write(str(msg))
'''
if __name__ == '__main__':
	a= "D:\\py\\automation_demo\\info\\['c5306b75']_cpu.txt"
	file_base().mkdir_file(a)
'''