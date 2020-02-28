#! /usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################################################
# pyserial   3.4
# Python 3.7.6rc1 (tags/v3.7.6rc1:bd18254b91, Dec 11 2019, 19:31:14) [MSC v.1916 32 bit (Intel)] on win32
#########################################################################################################
import time
import datetime
import threading
import binascii
import platform
import logging
import SerialDeal 
import serialMainUI
import serial
import wx
import wx.xrc

if platform.system() == "Windows":
    from serial.tools import list_ports
elif platform.system() == "Linux":
    import glob, os, re

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


class MainSerialUI(serialMainUI.serialFrame):
    def __init__(self, parent=None):
        super(MainSerialUI, self).__init__(parent)
        self.ser = None
        self.receive_count = 0
        self.receive_data = ""
        self.list_box_serial = None
        # self.port = None
        # self.baudrate = None
        # self.bytesize = None
        # self.stopbit = None
        #################################################################################################
        # methods for every widget
        #################################################################################################
        self.do_ui()
        #################################################################################################
        #################################################################################################

    def __del__(self):
        if platform.system() == "Linux":
            try:
                self.ser.SetStopEvent()
            except:
                pass

    def _debug_(self):
        plist = list(list_ports.comports())

        if len(plist) <= 0:
            print("The Serial port can't find!")
        else:
            plist_0 =list(plist[0])
            serialName = plist_0[0]
            serialFd = serial.Serial(serialName)
            print("check which port was really used >",serialFd.name)

    def do_ui(self):
        # 打开串口
        self.m_openser.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        # 关闭串口
        self.m_closeser.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        # 清空接受区
        self.m_clrRcvText.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        # 发送按钮1功能实现
        self.m_send1but.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        # 清空按钮1功能实现
        self.m_clr1but.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    def OnButtonClick(self, event):
        # 打开串口
        if event.GetEventObject() == self.m_openser:
            try:
                # port
                self.port = self.m_comset.GetValue()
                print("com is {}" .format(self.port))
                # baudrate
                self.baudrate = int(self.m_comboBox2.GetValue())
                print("buadrate is {}" .format(self.baudrate))
                # bytesize
                self.bytesize = int(self.m_comboBox3.GetValue())
                print("bytesize is {}" .format(self.bytesize))
                # parity
                self.parity = self.m_comboBox4.GetValue()
                print("parity is {}" .format(self.parity))
                if self.parity == u"None":
                    self.parity = serial.PARITY_NONE
                elif self.parity == u"Odd":
                    self.parity = serial.PARITY_ODD
                elif self.parity == u"Even":
                    self.parity = serial.PARITY_EVEN
                elif self.parity == u"Mark":
                    self.parity = serial.PARITY_MARK
                elif self.parity == u"Space":
                    self.parity = serial.PARITY_SPACE
                else:
                    print("parity error...")
                # stopbit
                self.stopbit = self.m_comboBox5.GetValue()
                print ("stopbit is {}" .format(self.stopbit))
                if self.stopbit == u"1":
                    self.stopbit = serial.STOPBITS_ONE
                elif self.stopbit == u"1.5":
                    self.stopbit = serial.STOPBITS_ONE_POINT_FIVE
                elif self.stopbit == u"2":
                    self.stopbit = serial.STOPBITS_TWO
                else:
                    print("stopbit error...")

                self.ser = SerialDeal.serDeal(Port=self.port,
                                            BaudRate=self.baudrate,
                                            ByteSize=self.bytesize,
                                            Parity=self.parity,
                                            Stopbits=self.stopbit)

                self.ser.start()
                print(u"opener --> self.ser.alive is {}" .format(self.ser.alive))
                if self.ser.alive:
                    print('success')
                    self.thread_read = threading.Thread(target=self.SerRead)
                    self.thread_read.setDaemon(True)
                    self.thread_read.start()
                    self.m_openser.Disable()
                    self.m_closeser.Enable()
            except serial.SerialException as e:
                logging.error(e)
                print(e)
                print(u'打开串口失败')
            event.Skip()

        # 关闭串口
        elif event.GetEventObject() == self.m_closeser:
            print(u"before : closer --> self.ser.alive is {}" .format(self.ser.alive))
            if self.ser.alive:
                self.ser.alive = False
            print(u"after : closer --> self.ser.alive is {}" .format(self.ser.alive))
            self.ser.close_serial()
            self.m_openser.Enable()
            self.m_closeser.Disable()

        # 清空接受区
        elif event.GetEventObject() == self.m_clrRcvText:
            print(u"接受区清空")
            self.m_rcvtext.Clear()
            print(u"Receive --> over")
            event.Skip()

        # 发送按钮1功能实现
        elif event.GetEventObject() == self.m_send1but:
            print(u"发送按钮1")
            try:
                if self.ser.alive:
                    send_data = ''
                    send_data += str(self.m_textCtrl5.GetValue())
                    self.ser.write(send_data)
                else:
                    wx.MessageBox(u"请注意，串口没有打开！！！", u"提示", wx.YES_NO | wx.CANCEL )
            except AttributeError as e:
                print(e)
                wx.MessageBox(u"请注意，串口没有打开！！！", u"提示", wx.YES_NO | wx.CANCEL )
            print(u"send 1 --> over")

        # 清空按钮1功能实现
        elif event.GetEventObject() == self.m_clr1but:
            print(u"清空按钮1")
            self.m_textCtrl5.Clear()
            print(u"clear 1 --> over")

    # 接收数据功能的实现

    def SerRead(self):
        while self.ser.alive:

            n = self.ser.serSer.inWaiting()
            try:
                self.receive_data = ""
                if n:
                    # print("self.ser.serSer.read(n) = {}" .format(self.ser.serSer.read(n)))
                    # print("self.m_rcvBox.GetValue() = {}" .format(self.m_rcvBox.GetValue()))
                    rev_data = self.ser.serSer.read(n).decode()
                    self.receive_data += rev_data.replace(binascii.unhexlify("00").decode(), "")
                    print("receive_data is {}" .format(self.receive_data))

                    # 接收显示是否为Hex
                    print("self.m_rcvBox.GetValue()={}, type is {}" .format(self.m_rcvBox.GetValue(), type(self.m_rcvBox.GetValue())))
                    if self.m_rcvBox.GetValue():
                        print("hex16")
                        print("self.receive_data = {}" .format(self.receive_data))
                        print("self.receive_data.encode()={}" .format(self.receive_data.encode()))
                        self.receive_data = self.space_b2a_hex(self.receive_data)
                        # self.receive_data = self.receive_data - 18
                    print("read5")
                    # ongoing
                    self.m_rcvtext.AppendText(self.receive_data)
                    self.receive_data = ""
            except Exception as e:
                logging.error(e)
                self.receive_data = ""
                self.ser.stop()
                self.ser = None

    def space_b2a_hex(self, data):
        """
        格式化接收到的数据字符串
         示例：123 --> 0x31 0x32 0x33 --> 49 50 51
        """
        new_data_list = []
        new_data = ""

        hex_data = binascii.b2a_hex(data.encode())
        temp_data = ""

        for index, value in enumerate(hex_data.decode()):
            temp_data += value
            if len(temp_data) >= 2:
                new_data_list.append(temp_data)
                temp_data = ""

        for index, value in enumerate(new_data_list):
            if index % 25 == 0 and index != 0:
                new_data += "\n"
            new_data += value
            new_data += " "
        print(u"new_data = {}" .format(new_data))
        return new_data


class SerialAPP(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的__init__，否则OnInit方法不会被调用
        wx.App.__init__(self)

    def OnInit(self):
        self.frame = MainSerialUI(None)
        self.frame.Show(True)

        return True


def main():
    App = SerialAPP()
    App.MainLoop()


if __name__ == '__main__':
    main()
