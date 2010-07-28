import wx
import wx.richtext
import string
import time

# create a big text
line = string.ascii_letters+"\n"
bigText = line*200000

app = wx.PySimpleApp()
myframe = wx.Frame(None)
#tc = wx.TextCtrl(myframe, style=wx.TE_MULTILINE)
tc = wx.richtext.RichTextCtrl(myframe)
def loadData():
    s = time.time()
    tc.SetMaxLength(len(bigText))
    tc.AppendText(bigText)
    print time.time()-s

# load big text after 5 secs
wx.CallLater(5000, loadData)

app.SetTopWindow(myframe)
myframe.Show()
app.MainLoop()
