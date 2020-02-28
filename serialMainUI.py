# -*- coding: utf-8 -*-
#########################################################################################################
# pyserial   3.4
# Python 3.7.6rc1 (tags/v3.7.6rc1:bd18254b91, Dec 11 2019, 19:31:14) [MSC v.1916 32 bit (Intel)] on win32
#########################################################################################################

import wx


class serialFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"串口助手", pos=wx.DefaultPosition,
                          size=wx.Size(559, 568), style=wx.DEFAULT_FRAME_STYLE)

        self.panel = wx.Panel(self, -1)

        # 在屏幕中央显示界面
        self.CenterOnScreen()

        ################################################################################################################
        ################################################################################################################
        sergrid = wx.GridBagSizer(0, 0)
        sergrid.SetFlexibleDirection(wx.BOTH)
        sergrid.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self.panel, wx.ID_ANY, u"串口选择", wx.Point(1, 1), wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        sergrid.Add(self.m_staticText1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_rcvtext = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, 200),
                                     wx.TE_AUTO_URL | wx.TE_LEFT | wx.TE_MULTILINE)
        sergrid.Add(self.m_rcvtext, wx.GBPosition(0,2), wx.GBSpan(8,2), wx.ALL, 6)

        self.m_send2but = wx.Button(self.panel, wx.ID_ANY, u"发送2", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add( self.m_send2but, wx.GBPosition(9, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_clr2but = wx.Button(self.panel, wx.ID_ANY, u"清空2", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_clr2but, wx.GBPosition(9, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_send3but = wx.Button(self.panel, wx.ID_ANY, u"发送3", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_send3but, wx.GBPosition(10, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_clr3but = wx.Button(self.panel, wx.ID_ANY, u"清空3", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add( self.m_clr3but, wx.GBPosition( 10, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_send3but = wx.Button(self.panel, wx.ID_ANY, u"发送4", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_send3but, wx.GBPosition(11, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_clr4but = wx.Button(self.panel, wx.ID_ANY, u"清空4", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_clr4but, wx.GBPosition(11, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_send5but = wx.Button(self.panel, wx.ID_ANY, u"发送5", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_send5but, wx.GBPosition(12, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_clr5but = wx.Button(self.panel, wx.ID_ANY, u"清空5", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_clr5but, wx.GBPosition(12, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_send6but = wx.Button(self.panel, wx.ID_ANY, u"发送6", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_send6but, wx.GBPosition(13, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_clr6but = wx.Button(self.panel, wx.ID_ANY, u"清空6", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_clr6but, wx.GBPosition(13, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        m_comsetChoices = [u"COM1", u"COM2", u"COM3", u"COM4", u"COM5", u"COM6", u"COM7", u"COM8", u"COM9", u"COM10"]
        self.m_comset = wx.ComboBox(self.panel, wx.ID_ANY, u"COM1", wx.DefaultPosition, wx.DefaultSize, m_comsetChoices,
                                    0)
        self.m_comset.SetSelection(0)
        sergrid.Add(self.m_comset, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_openser = wx.Button(self.panel, wx.ID_ANY, u"打开串口", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add( self.m_openser, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 8)

        self.m_clrRcvText = wx.Button(self.panel, wx.ID_ANY, u"清空接收", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_clrRcvText, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_rcvBox = wx.CheckBox(self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_rcvBox, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_send1but = wx.Button(self.panel, wx.ID_ANY, u"发送1", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_send1but, wx.GBPosition(8, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_clr1but = wx.Button(self.panel, wx.ID_ANY, u"清空1", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add( self.m_clr1but, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                                    wx.HSCROLL | wx.TE_AUTO_URL)
        sergrid.Add(self.m_textCtrl5, wx.GBPosition(8, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox2 = wx.CheckBox( self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox2.SetValue(True)
        sergrid.Add( self.m_checkBox2, wx.GBPosition(8, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox3 = wx.CheckBox(self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox3.SetValue(True)
        sergrid.Add(self.m_checkBox3, wx.GBPosition(9, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox4 = wx.CheckBox(self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox4.SetValue(True)
        sergrid.Add(self.m_checkBox4, wx.GBPosition(10, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox5 = wx.CheckBox(self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox5.SetValue(True)
        sergrid.Add(self.m_checkBox5, wx.GBPosition(11, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox6 = wx.CheckBox(self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox6.SetValue(True)
        sergrid.Add(self.m_checkBox6, wx.GBPosition(12, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_checkBox7 = wx.CheckBox(self.panel, wx.ID_ANY, u"16进制", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox7.SetValue(True)
        sergrid.Add(self.m_checkBox7, wx.GBPosition(13, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sergrid.Add(self.m_textCtrl6, wx.GBPosition(9, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sergrid.Add(self.m_textCtrl7, wx.GBPosition(10, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sergrid.Add(self.m_textCtrl8, wx.GBPosition(11, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sergrid.Add(self.m_textCtrl9, wx.GBPosition(12, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        sergrid.Add(self.m_textCtrl10, wx.GBPosition(13, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_closeser = wx.Button(self.panel, wx.ID_ANY, u"关闭串口", wx.DefaultPosition, wx.DefaultSize, 0)
        sergrid.Add(self.m_closeser, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self.panel, wx.ID_ANY, u"校验位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        sergrid.Add(self.m_staticText6, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self.panel, wx.ID_ANY, u"停止位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        sergrid.Add(self.m_staticText7, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_comboBox4Choices = [u"None", u"Odd", u"Even", u"Mark", u"Space"]
        self.m_comboBox4 = wx.ComboBox(self.panel, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize,
                                    m_comboBox4Choices, 0)
        sergrid.Add(self.m_comboBox4, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        m_comboBox5Choices = [u"1", u"1.5", u"2"]
        self.m_comboBox5 = wx.ComboBox(self.panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize,
                                    m_comboBox5Choices, 0)
        sergrid.Add(self.m_comboBox5, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self.panel, wx.ID_ANY, u"数据位：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        sergrid.Add( self.m_staticText5, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        m_comboBox2Choices = [u"9600", u"19200", u"38400", u"57600", u"115200", u"230400", u"460800", u"921600",
                            wx.EmptyString, wx.EmptyString]
        self.m_comboBox2 = wx.ComboBox(self.panel, wx.ID_ANY, u"9600", wx.DefaultPosition, wx.DefaultSize,
                                    m_comboBox2Choices, 0)
        sergrid.Add(self.m_comboBox2, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        m_comboBox3Choices = [ u"8", u"7", u"6", u"5" ]
        self.m_comboBox3 = wx.ComboBox(self.panel, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize,
                                    m_comboBox3Choices, 0)
        sergrid.Add(self.m_comboBox3, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.panel, wx.ID_ANY, u"波特率：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        sergrid.Add(self.m_staticText4, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        ################################################################################################################
        # layout
        self.panel.SetSizerAndFit(sergrid)
        self.panel.Layout()

        self.Centre(wx.BOTH)
        ################################################################################################################
        ################################################################################################################


class SerialAPP(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的__init__，否则OnInit方法不会被调用
        wx.App.__init__(self)

    def OnInit(self):
        self.frame = serialFrame(None)
        self.frame.Show(True)

        return True

# 主函数


if __name__ == "__main__":
    app = SerialAPP()
    # 循环监听事件
    app.MainLoop()
