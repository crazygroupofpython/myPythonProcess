# coding=gbk
import psutil
 
#�г����н��̵�PID
pids = psutil.pids()
exe = "pcik_15_dbc_x86_singalsave.exe"

for pid in pids:
	try:
		p = psutil.Process(pid)				
		print(pid,p.exe())
	except Exception as e:
		print(e)
	 
	#��ȡ����bin��·��
	#try:
	#	print(p.exe())
	#except:
	#	pass
	#��ȡ���̹���Ŀ¼����·��
	#try:
	#	print(p.cwd())
	#except:
	#	pass
	
strs = input("������q�˳�:")
while True:
	if strs.lower() == "q":
		break
		
	strs = input("������q�˳�:")
	 
	#���̵�״̬
	#print(p.status())
	""" 
	#��ȡ����bin��·��
	print(p.exe())
			
	#��ȡ���̹���Ŀ¼����·��
	print(p.cwd())
	
	#���̴�����ʱ��
	print(p.create_time())
	 
	#����uid��Ϣ
	print(p.uids())
	 
	#����gid��Ϣ
	print(p.gids())
	 
	#����CPUʱ����Ϣ������user��system����CPUʱ��
	print(p.cpu_times())
	 
	#��ȡ����cpu���׺Ͷ�
	print(p.cpu_affinity())
	 
	#��ȡ�����ڴ�������
	print(p.memory_percent())
	 
	#�����ڴ�rss��vms��Ϣ
	print(p.memory_info())
	 
	#����IO��Ϣ��������дIO�����ֽ���
	print(p.io_counters())
	 
	#��ȡ�򿪽���socket��namedutples�б�����fs��family��laddr����Ϣ
	print(p.connections())
	 
	#���̿������߳���
	print(p.num_threads())"""

