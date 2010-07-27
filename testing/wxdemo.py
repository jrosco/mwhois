#!/usr/bin/python

# simplemenu.py

import wx

class SimpleMenu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 150))

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(-1, 'Quit', 'Quit application')
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)

        self.Centre()
        self.Show(True)

app = wx.App()
SimpleMenu(None, -1, 'simple menu example')
app.MainLoop()
