#!/usr/bin/env python

import wx


class AboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.NullBitmap)
        self.label_txt = wx.StaticText(self, -1, "Author: Joel Cumberland\n" \
            "Version: 0.1.10a Alpha\n" \
            "Website: jrosco.github.io/mwhois/\n" \
            "Email: joel_c@zoho.com")
        self.button_close = wx.Button(self, -1, "Close")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.close_app, self.button_close)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle("About mwhois")
        # end wxGlade


AboutDialog()