# coding=gbk
#�ο���ַhttps://blog.csdn.net/wy_97/article/details/79663014

import ctypes,sys
class Set_Color():
	STD_INPUT_HANDLE = -10
	STD_OUTPUT_HANDLE = -11
	STD_ERROR_HANDLE = -12

	# ������ɫ���� ,�ؼ�������ɫ���룬��2λʮ��������ɣ��ֱ�ȡ0~f��ǰһλָ���Ǳ���ɫ����һλָ��������ɫ
	#���ڸú��������ƣ�Ӧ����ֻ����16�֣�����ǰ��ɫ�뱳��ɫ��ϡ�Ҳ���Լ�����ɫͨ����������ϣ���Ϻ�������16����ɫ��

	# Windows CMD������ ������ɫ���� text colors
	FOREGROUND_BLACK = 0x00 # black.
	FOREGROUND_DARKBLUE = 0x01 # dark blue.
	FOREGROUND_DARKGREEN = 0x02 # dark green.
	FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
	FOREGROUND_DARKRED = 0x04 # dark red.
	FOREGROUND_DARKPINK = 0x05 # dark pink.
	FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
	FOREGROUND_DARKWHITE = 0x07 # dark white.
	FOREGROUND_DARKGRAY = 0x08 # dark gray.
	FOREGROUND_BLUE = 0x09 # blue.
	FOREGROUND_GREEN = 0x0a # green.
	FOREGROUND_SKYBLUE = 0x0b # skyblue.
	FOREGROUND_RED = 0x0c # red.
	FOREGROUND_PINK = 0x0d # pink.
	FOREGROUND_YELLOW = 0x0e # yellow.
	FOREGROUND_WHITE = 0x0f # white.


	# Windows CMD������ ������ɫ���� background colors
	BACKGROUND_BLUE = 0x10 # dark blue.
	BACKGROUND_GREEN = 0x20 # dark green.
	BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
	BACKGROUND_DARKRED = 0x40 # dark red.
	BACKGROUND_DARKPINK = 0x50 # dark pink.
	BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
	BACKGROUND_DARKWHITE = 0x70 # dark white.
	BACKGROUND_DARKGRAY = 0x80 # dark gray.
	BACKGROUND_BLUE = 0x90 # blue.
	BACKGROUND_GREEN = 0xa0 # green.
	BACKGROUND_SKYBLUE = 0xb0 # skyblue.
	BACKGROUND_RED = 0xc0 # red.
	BACKGROUND_PINK = 0xd0 # pink.
	BACKGROUND_YELLOW = 0xe0 # yellow.
	BACKGROUND_WHITE = 0xf0 # white.

	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	# get handle
	

	def set_cmd_text_color(self,color, handle=False):
		if handle:
			Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
		else:
			Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(self.std_out_handle, color)
		return Bool

	#reset white
	def resetColor(self):
		self.set_cmd_text_color(self.FOREGROUND_GREEN)

	#reset white
	def resetDefault(self):
		self.set_cmd_text_color(self.FOREGROUND_RED | self.FOREGROUND_GREEN | self.FOREGROUND_BLUE)
    
	###############################################################

	#����ɫ
	#dark blue
	def printDarkBlue(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKBLUE)
		sys.stdout.write(mess)
		self.resetColor()

	#����ɫ
	#dark green
	def printDarkGreen(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKGREEN)
		sys.stdout.write(mess)
		self.resetColor()

	#������ɫ
	#dark sky blue
	def printDarkSkyBlue(mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKSKYBLUE)
		sys.stdout.write(mess)
		self.resetColor()

	#����ɫ
	#dark red
	def printDarkRed(self,mess):
		#self.set_back()
		self.set_cmd_text_color(self.FOREGROUND_DARKRED)
		sys.stdout.write(mess)
		self.resetColor()

	#���ۺ�ɫ
	#dark pink
	def printDarkPink(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKPINK)
		sys.stdout.write(mess)
		self.resetColor()

	#����ɫ
	#dark yellow
	def printDarkYellow(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKYELLOW)
		sys.stdout.write(mess)
		self.resetColor()

	#����ɫ
	#dark white
	def printDarkWhite(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKWHITE)
		sys.stdout.write(mess)
		self.resetColor()

	#����ɫ
	#dark gray
	def printDarkGray(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_DARKGRAY)
		sys.stdout.write(mess)
		self.resetColor()

	#��ɫ
	#blue
	def printBlue(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_BLUE)
		sys.stdout.write(mess)
		self.resetColor()

	#��ɫ
	#green
	def printGreen(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_GREEN)
		sys.stdout.write(mess)
		self.resetColor()

	#����ɫ
	#sky blue
	def printSkyBlue(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_SKYBLUE)
		sys.stdout.write(mess)
		self.resetColor()

	#��ɫ
	#red
	def printRed(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_RED)
		sys.stdout.write(mess)
		self.resetColor()

	#�ۺ�ɫ
	#pink
	def printPink(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_PINK)
		sys.stdout.write(mess)
		self.resetColor()

	#��ɫ
	#yellow
	def printYellow(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_YELLOW)
		sys.stdout.write(mess)
		self.resetColor()

	#��ɫ
	#white
	def printWhite(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_WHITE)
		sys.stdout.write(mess)
		self.resetColor()

	##################################################

	#�׵׺���
	#white bkground and black text
	def printWhiteBlack(self,mess):
		self.set_cmd_text_color(self.FOREGROUND_BLACK | self.BACKGROUND_WHITE)
		sys.stdout.write(mess)
		self.resetColor()

	#�׵׺���
	#white bkground and black text
	def printWhiteBlack_2(self,mess):
		self.set_cmd_text_color(0xf0)
		sys.stdout.write(mess)
		self.resetColor()


	#�Ƶ�����
	#white bkground and black text
	def printYellowRed(self,mess):
		self.set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
		sys.stdout.write(mess)
		self.resetColor()


	##############################################################
	"""
	if __name__ == '__main__':

		print
		printDarkBlue('printDarkBlue:����ɫ����\n')
		printDarkGreen('printDarkGreen:����ɫ����\n')
		printDarkSkyBlue(u'printDarkSkyBlue:������ɫ����\n')
		printDarkRed(u'printDarkRed:����ɫ����\n')
		printDarkPink(u'printDarkPink:���ۺ�ɫ����\n')
		printDarkYellow(u'printDarkYellow:����ɫ����\n')
		printDarkWhite(u'printDarkWhite:����ɫ����\n')
		printDarkGray(u'printDarkGray:����ɫ����\n')
		printBlue(u'printBlue:��ɫ����\n')
		printGreen(u'printGreen:��ɫ����\n')
		printSkyBlue(u'printSkyBlue:����ɫ����\n')
		printRed(u'printRed:��ɫ����\n')
		printPink(u'printPink:�ۺ�ɫ����\n')
		printYellow(u'printYellow:��ɫ����\n')
		printWhite(u'printWhite:��ɫ����\n')
		printWhiteBlack(u'printWhiteBlack:�׵׺������\n')
		printWhiteBlack_2(u'printWhiteBlack_2:�׵׺������\n')
		printYellowRed('printYellowRed:�Ƶ׺������\n')
	 """
#c = Set_Color()
#c.printDarkRed(u'printDarkRed:����ɫ����\n')
