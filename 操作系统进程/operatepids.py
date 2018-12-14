# coding=gbk
import psutil
import os
from shutil import copytree
import time
import re
#shutil.copytree(src, dst, symlinks=False, ignore=None, 
#copy_function=copy2, ignore_dangling_symlinks=False)

class Operate_Pids():
	#��Ӫ������,php����
	filename = "runservers.ini"
	
	#��������
	command = 'taskkill /F  /PID {}'
	
	#�����ļ�·��
	basepath = "D:\\example\\test\\base_ver"
	
	#Ŀ��Ŀ¼
	dstpath = "D:\\example\\test\\{}"
	
	#cfg�����ļ�
	cfgfile = "D:\\example\\test\\{}\\cfg\\example.ini"
	
	#��������·��
	exe_path = "D:\\example\\test\\{}\\notepad.exe"
	
	#����Ĭ�ϳ�����	
	def __init__(self,pidname='notepad.exe'):
		self.pidname = pidname
	
	#ɸѡ��ָ������	
	def getPid(self):
		pids = psutil.pids()
		pidspath={}
		for pid in pids:
			try:
				p = psutil.Process(pid)
				serverid = 	self.getPidId(p.exe())
				if self.pidname == p.name() and serverid:
					#print(p.exe(),p.name())
					pidspath[pid]=serverid
			except Exception as e:
				#print(e)
				pass
		return pidspath
	
	
	#��ȡ��������Ŀ¼�ı��
	def getPidId(self,pidpath):
		#print(pidpath)
		return pidpath.split('\\')[-2] if os.path.exists(pidpath) else False
	
	#����Ŀ¼ģ��
	def pidTemplate(self,serverid):
		return self.dstpath.format(serverid)
		
	#��������ID
	def killPid(self,pids):
		if len(pids) > 0:
			for pid in pids:
				#print('�ɹ���������:{}'.format(pid))
				os.system(self.command.format(pid))
	
	
	#��ʽ��serverid
	def getServerId(self):
		data = self.getDataFromFile()
		
		if data:
			return set(filter(lambda x:x.strip(),data.split("\n")))
		else:
			return set()
		
		
	#��ȡ�ļ�����Ӫ������id
	def getDataFromFile(self):
		if os.path.exists(self.filename):
			try:
				with open(self.filename,'r') as f:
					return f.read().strip('\n')
			except Exception as e:
				print(e)
				return False
		else:
			return False
	
	
	def cpBaseFile(self,dst):
		try:
			copytree(self.basepath,dst)
		except Exception as e:
			print(e)
			pass
	
	
	def mkdirs(self,dirpath):
		dt = time.strftime(" %Y-%m-%d %H-%M-%S",time.localtime())
		if os.path.exists(dirpath):
			try:
				os.rename(dirpath,dirpath+dt)
			except Exception as e:
				print(e)
				pass
		#os.makedirs(dirpath)
	
	
	def createDir(self,servers):
		for serid in servers:
			path = self.pidTemplate(serid)#��ȡĿ��Ŀ¼
			print(path)
			
			self.mkdirs(path)#������Ŀ¼
			self.cpBaseFile(path)#�����ļ�
			self.changeGameIni(serid)#���������ļ�
			self.run(serid)#��������
	
	
	def run(self,serid):
		exe_path = self.exe_path.format(serid)
		os.startfile(exe_path)
		
		
	#����server id���������ļ�����		
	def changeGameIni(self,serid):
		path = self.cfgfile.format(serid)
		self.writeIni(self.defineRe(self.readIni(path),serid),path)
	
	
	#�����滻�������
	def writeIni(self,content,path):
		try:
			with open(path,'w') as f:
				f.write(content)
				f.close()
		except Exception as e:
			print(e)

	
	#�滻�ļ��ƶ�����
	def defineRe(self,txt,serid):
		try:
			txt = re.sub(r'port=2\d+','port=2'+str(serid),txt)
			txt = re.sub(r'groupid=\d+','groupid='+str(serid),txt)
		except Exception as e:
			print(e)
		else:
			return txt
	
	#��ȡ�����ļ�����	
	def readIni(self,path):
		try:
			with open(path,'r') as f:
				txt = f.read()
				f.close()
		except Exception as e:
			print(e)
		else:
			return txt
			
			
	def getdiffeId(self,src,dst):
		return src - dst
	
	#��ȡ��Ҫ�رյĽ���ID
	def getPidBySerId(self,pids,sers):
		waitpids = list()
		for k,v in pids.items():
			for ser in sers:
				if ser == v:
					waitpids.append(k)
		return waitpids
	
	def main(self):
		pids = self.getPid()
		#print(pids)
		#�����·�
		self.createDir(self.getdiffeId(self.getServerId(),set(pids.values())))
		
		#�رվɷ�
		waitkillserid = self.getdiffeId(set(pids.values()),self.getServerId())
		#print(waitkillserid)
		waitkillpid = self.getPidBySerId(pids,waitkillserid)
		self.killPid(waitkillpid)
		
	
pids = Operate_Pids()
pids.main()


strs = input("������q�˳�:")
while True:
	if strs.lower() == "q":
		break		
	strs = input("������q�˳�:")
