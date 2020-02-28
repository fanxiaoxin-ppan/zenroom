# -*- coding: utf-8 -*-
import wx
import binascii

data = u"55AA08060100024D5E77"
print data

class MyFrame(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id , title = u'binascii demo frame', size = (500, 230))
		
		self.panel = wx.Panel(self, -1)
		
		wx.StaticText(self.panel, -1, u"请输入一个字符串 ： ", (20, 20), (-1, 20))
		self.hexlifyTC = wx.TextCtrl(self.panel, -1, wx.EmptyString, (138, 20), (300, 20))
		
		self.hexlifyButton = wx.Button(self.panel, -1, u' hexlify ', (20, 50), (60, 25))
		self.hexlifyST = wx.StaticText(self.panel, -1, wx.EmptyString, (90, 55), (-1, 20))
		
		wx.StaticText(self.panel, -1, u"请输入一个字符串 ： ", (20, 90), (-1, 20))
		self.unhexlifyTC = wx.TextCtrl(self.panel, -1, wx.EmptyString, (138, 90), (300, 20))
		
		self.unhexlifyButton = wx.Button(self.panel, -1, u' unhexlify ', (20, 140), (60, 25))
		self.unhexlifyST = wx.StaticText(self.panel, -1, wx.EmptyString, (90, 145), (-1, 20))
		
		self.Bind(wx.EVT_BUTTON, self.OnClickButton, self.hexlifyButton)
		self.Bind(wx.EVT_BUTTON, self.OnClickButton, self.unhexlifyButton)
	
	def OnClickButton(self, event):
		if event.GetEventObject() == self.hexlifyButton:
			print u"self.hexlifyButton"
			ct = self.hexlifyTC.GetValue()
			res = binascii.hexlify(ct).decode('utf-8')
			self.hexlifyST.SetLabelText(u"{}" .format(res))
		elif event.GetEventObject() == self.unhexlifyButton:
			print u"self.unhexlifyButton"
			try:
				ct = self.unhexlifyTC.GetValue()
				res = binascii.unhexlify(ct).decode(encoding="utf-8", errors="strict")
				self.unhexlifyST.SetLabelText(res)
			except (TypeError, UnicodeDecodeError) as e:
				wx.MessageBox(u"{}" .format(e), u"提示错误信息")
		else:
			wx.MessageBox(u"按钮点击错误，请排查。", u"提示信息")

class MyApp(wx.App):
	def __init__(self):
		wx.App.__init__(self)
	
	def OnInit(self):
		self.frame = MyFrame(None, -1)
		self.frame.Center()
		self.frame.Show(True)
		
		return True

def main():
	app = MyApp()
	app.MainLoop()

if __name__ == "__main__":
	main()