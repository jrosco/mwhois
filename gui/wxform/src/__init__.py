import wx
from main import MainGUI

__author__ = 'jrosco'
__version__ = '1.0b'

""" Main run """
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainGUI(None)
    frame.Show(True)
    app.MainLoop()
