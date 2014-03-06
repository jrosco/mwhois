#!/usr/bin/env python

import wx


class AboutDialog(wx.Dialog):

    def __init__(self, *args, **kwds):

        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.NullBitmap)
        self.label_txt = wx.StaticText(self, -1, "Author: jrosco\n"
            "Version: 0.1.0b Beta\n"
            "Website: http://jrosco.github.io/mwhois/\n"
            "Email: joel_c@zoho.com")
        self.button_close = wx.Button(self, -1, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.close_app, self.button_close)

    def __set_properties(self):

        self.SetTitle("About Multi Whois")

    def __do_layout(self):

        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(self.bitmap_1, 0, 0, 0)
        sizer_13.Add(self.label_txt, 0, 0, 0)
        sizer_12.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_14.Add(self.button_close, 0, 0, 0)
        sizer_12.Add(sizer_14, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_12)
        sizer_12.Fit(self)
        self.Layout()

    def close_app(self, event):

        wx.Dialog.Close(self, force=True)