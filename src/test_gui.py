import wx
from test_file import *

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.text_ctrl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.button = wx.Button(self, -1, "button")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.do_it, self.button)
        
    def __set_properties(self):
        self.SetTitle("frame")
        self.text_ctrl.SetMinSize((300, 200))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.text_ctrl, 0, 0, 0)
        sizer_1.Add(self.button, 0, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

    def do_it(self, event): 
        self.foo = get_line()            
        self.bar = self.foo.line("C:/test", self.text_ctrl)

    def return_textbox(self):
        return_box = self.text_ctrl
        return return_box

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame = MyFrame(None, -1, "")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()