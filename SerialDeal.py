# -*- coding: utf-8 -*-
#########################################################################################################
# pyserial   3.4
# Python 3.7.6rc1 (tags/v3.7.6rc1:bd18254b91, Dec 11 2019, 19:31:14) [MSC v.1916 32 bit (Intel)] on win32
#########################################################################################################
import os
import time
from time import *
import binascii
import logging
import serial

cwd = os.getcwd()
print(cwd)


class serDeal(object):
	def __init__(self, Port="COM6", BaudRate=9600, ByteSize=8, Parity="N", Stopbits=1, timeout=None,
				xonxof=0, rtscts=0):
		self.serSer = None
		self.alive = False
		self.port = Port
		self.baudrate = BaudRate
		self.bytesize = ByteSize
		self.parity = Parity
		self.stopbits = Stopbits
		self.timeout = timeout
		self.thresholdValue = 64
		self.receive_data = ""
	
	def start(self):
		self.serSer = serial.Serial()
		self.serSer.port = self.port
		self.serSer.baudrate= self.baudrate
		self.serSer.bytesize = self.bytesize
		self.serSer.parity = self.parity
		self.serSer.stopbits = self.stopbits
		self.serSer.timeout = self.timeout
		
		try:
			self.serSer.open()
			if self.serSer.isOpen():
				self.alive = True
		except Exception as e:
			self.alive = False
			logging.error(e)
	
	def stop(self):
		while self.alive:
			try:
				number = self.serSer.inWaiting()
				if number:
					self.receive_data += self.serSer.read(number).decode().replace(binascii.unhexlify("00").decode(), "")
					if self.thresholdValue <= len(self.receive_data):
						self.receive_data = ""
			except Exception as e:
				logging.error(e)
	
	def readcom(self):
		# we can deal with the UART output
		clear_time = 0
		while 1:
			sleep(0.05)
			reading = self.serSer.readall()
			if len(reading) > 0:
				LOG = self.serSer.port + ":" + reading
				print(LOG)
				self.__conservelog(LOG)
				clear_time = 0
			else:
				clear_time = clear_time + 1

			if clear_time > 10:
				break
	
	def write(self, data, isHex=False):
		if self.alive:
			if self.serSer.isOpen:
				if isHex:
					data = binascii.unhexlify(data)
					print(data)
				print(data)
				print(data.encode())
				self.serSer.write(data.encode())
	
	# support input from Console
	def write_serial_con(self):
		while 1:
			command = input()
			for character in command:
				self.serSer.write(character)
			self.serSer.write('\r')
	
	def write_serial(self, command):
		for character in command:
			self.serSer.write(character)
		self.serSer.write('\r')
		self.readcom()
				
	# 发送指令的完整流程
	def send_cmd(self, cmd):
		self.port.write(cmd)
		response = self.port.readall()
		response = self.convert_hex(response)
		return response
	
	# 转成16进制的函数
	def convert_hex(self, string):
		res = []
		result = []
		for item in string:
			res.append(item)
		for i in res:
			result.append(hex(i))
		
		return result
	
	def __conservelog(self, read_data):
		with open('testlog', 'a+') as writelog:
			writelog.write(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))+': '+read_data+'\r')
	
	def close_serial(self):
		self.serSer.close()

	'''
	# 打开端口
        self.port = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='E', stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)
        return response

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result
	
	def hexShow(argv):
		result = ''
		hLen = len(argv)
		for i in xrange(hLen):
			hvol = ord(argv[i])
			hhex = '%02x'%hvol
			result += hhex+' '
	其中，read(value)方法的参数value为需要读取的字符长度。 如果想要全部读取，提供两个方法：
	1）inWaiting：：监测接收字符。 inWaitting返回接收字符串的长度值，然后把这个值赋给read做参数。
	2）readall（）：：读取全部字符。
	
	def hexsend(string_data=''):
		hex_data = string_data.decode("hex")
		return hex_data
	'''