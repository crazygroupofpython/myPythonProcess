# coding=gbk
import os

class Save():
	path="./download/"
	count = 0
	
	def __init__(self):
		self.mkdir(self.path)
	
	def save(self,contents,name):
		if contents and name:
			try:
				with open(self.remove_special_characters(name),'wb') as f:
					f.write(contents)
			except Exception as e:
				print(e)
				pass
			else:
				self.count+=1
	#�����ļ����Ŀ¼
	def mkdir(self,path):
		if os.path.exists(path):
			return
		os.makedirs(path)
	
	#��ֹ�ظ�����	
	def checkfile(self,name):
		if name == 'temp':
			return
		return os.path.exists(self.remove_special_characters(name))
	
	#ȷ��windows���ļ��ɴ����ɹ�
	def remove_special_characters(self,string):
		#windows�ļ����в��������з��ţ�'\\', '/', ':', '*', '?', '"', '<', '>', '|'
		special_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
		for special_character in special_characters:
			string = string.replace(special_character,'')
		return '/'.join([self.path.strip('/'),string.strip()])+".mp3"
		
		
		
		
