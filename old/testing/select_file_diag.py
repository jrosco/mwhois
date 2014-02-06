import wx

dirname = ''
dlg = wx.FileDialog("Choose a file", dirname,"","*.*", wx.OPEN)
if dlg.ShowModal()== wx.ID_OK:
    filename = dlg.GetFilename()
    Fname = filename
    dirname=dlg.GetDirectory()
dlg.Destroy()