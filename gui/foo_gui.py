#!/usr/bin/env python
# -*- coding: ISO-8859-15 -*-
#
# generated by wxGlade 0.6.7+ on Sat Jan 18 17:53:05 2014
#

import wx
import wx.grid

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyApp(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyApp.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=0)
        self.notebook_1_pane = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.single_lbl = wx.StaticText(self.notebook_1_pane, wx.ID_ANY, _("Enter domain Name:"), style=wx.ALIGN_CENTRE)
        self.single_txt = wx.TextCtrl(self.notebook_1_pane, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.single_button = wx.Button(self.notebook_1_pane, wx.ID_ANY, _("Single Search"))
        self.single_txt_area = wx.TextCtrl(self.notebook_1_pane, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.single_quit_btn = wx.Button(self.notebook_1_pane, wx.ID_ANY, _("Quit"))
        self.sizer_1_staticbox = wx.StaticBox(self.notebook_1_pane, wx.ID_ANY, _("mwhois"))
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.input_lbl = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, _("Input Wordlist:"))
        self.input_txt = wx.TextCtrl(self.notebook_1_pane_2, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.input_btn = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, _("Open"))
        self.save_lbl = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, _("Output Domainlist:"))
        self.save_txt = wx.TextCtrl(self.notebook_1_pane_2, wx.ID_ANY, "")
        self.save_btn = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, _("Save"))
        self.adv_txt = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, _("Advanced Search:"))
        self.adv_chkbox = wx.CheckBox(self.notebook_1_pane_2, wx.ID_ANY, "")
        self.tld_lbl = wx.StaticText(self.notebook_1_pane_2, wx.ID_ANY, _("Select TLD:"))
        self.tld_cumbo = wx.ComboBox(self.notebook_1_pane_2, wx.ID_ANY, choices=[_("com"), _("net"), _("edu"), _("biz")], style=wx.CB_DROPDOWN)
        self.grid_2 = wx.grid.Grid(self.notebook_1_pane_2, wx.ID_ANY, size=(1, 1))
        self.begin_btn = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, _("Begin"))
        self.adv_quit_btn = wx.Button(self.notebook_1_pane_2, wx.ID_ANY, _("Quit"))
        self.sizer_5_staticbox = wx.StaticBox(self.notebook_1_pane_2, wx.ID_ANY, _("mwhois"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.single_search, self.single_button)
        self.Bind(wx.EVT_BUTTON, self.close_app, self.single_quit_btn)
        self.Bind(wx.EVT_BUTTON, self.open_file, self.input_btn)
        self.Bind(wx.EVT_BUTTON, self.save_file, self.save_btn)
        self.Bind(wx.EVT_CHECKBOX, self.adv_search, self.adv_chkbox)
        self.Bind(wx.EVT_COMBOBOX, self.get_tld, self.tld_cumbo)
        self.Bind(wx.EVT_BUTTON, self.multi_search, self.begin_btn)
        self.Bind(wx.EVT_BUTTON, self.close_app, self.adv_quit_btn)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyApp.__set_properties
        self.SetTitle(_("mwhois widget"))
        self.SetSize((550, 642))
        self.single_lbl.SetMinSize((130, 14))
        self.single_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.single_txt.SetMinSize((178, 21))
        self.single_txt.SetFocus()
        self.single_button.SetMinSize((99, 23))
        self.single_txt_area.SetMinSize((524, 483))
        self.single_txt_area.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.input_lbl.SetMinSize((120, 13))
        self.input_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.input_txt.SetMinSize((200, 21))
        self.save_lbl.SetMinSize((120, 13))
        self.save_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.save_txt.SetMinSize((200, 21))
        self.adv_txt.SetMinSize((120, 20))
        self.adv_txt.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.adv_chkbox.SetMinSize((25, 13))
        self.tld_lbl.SetMinSize((80, 13))
        self.tld_lbl.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.tld_cumbo.SetMinSize((50, 21))
        self.tld_cumbo.SetForegroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_DESKTOP))
        self.tld_cumbo.SetSelection(-1)
        self.grid_2.CreateGrid(0, 2)
        self.grid_2.SetRowLabelSize(30)
        self.grid_2.SetColLabelSize(30)
        self.grid_2.EnableGridLines(0)
        self.grid_2.EnableDragRowSize(0)
        self.grid_2.SetGridLineColour(wx.Colour(255, 255, 255))
        self.grid_2.SetLabelBackgroundColour(wx.Colour(255, 255, 255))
        self.grid_2.SetColLabelValue(0, _("Domain"))
        self.grid_2.SetColSize(0, 250)
        self.grid_2.SetColLabelValue(1, _("Status"))
        self.grid_2.SetColSize(1, 245)
        self.notebook_1.SetMinSize((550, 100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyApp.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_5_staticbox.Lower()
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_1_staticbox.Lower()
        sizer_1 = wx.StaticBoxSizer(self.sizer_1_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.single_lbl, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.single_txt, 0, 0, 0)
        sizer_2.Add(self.single_button, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_2, 0, 0, 0)
        sizer_3.Add(self.single_txt_area, 60, wx.EXPAND, 0)
        sizer_3.Add(self.single_quit_btn, 0, wx.ALIGN_RIGHT, 0)
        sizer_1.Add(sizer_3, 100, wx.EXPAND, 0)
        self.notebook_1_pane.SetSizer(sizer_1)
        sizer_7.Add(self.input_lbl, 0, 0, 0)
        sizer_7.Add(self.input_txt, 0, 0, 0)
        sizer_7.Add(self.input_btn, 0, 0, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.save_lbl, 0, 0, 0)
        sizer_8.Add(self.save_txt, 0, 0, 0)
        sizer_8.Add(self.save_btn, 0, 0, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_9.Add(self.adv_txt, 0, 0, 0)
        sizer_9.Add(self.adv_chkbox, 0, 0, 0)
        sizer_9.Add(self.tld_lbl, 0, 0, 0)
        sizer_9.Add(self.tld_cumbo, 0, 0, 0)
        sizer_6.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_11.Add(self.grid_2, 0, wx.EXPAND, 0)
        sizer_6.Add(sizer_11, 0, wx.EXPAND, 0)
        sizer_10.Add(self.begin_btn, 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 0)
        sizer_10.Add(self.adv_quit_btn, 0, wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM, 0)
        sizer_6.Add(sizer_10, 1, wx.ALIGN_RIGHT, 0)
        sizer_5.Add(sizer_6, 10, 0, 0)
        self.notebook_1_pane_2.SetSizer(sizer_5)
        self.notebook_1.AddPage(self.notebook_1_pane, _("Single Search"))
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Multi Search"))
        sizer_4.Add(self.notebook_1, 17, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        self.Centre()
        # end wxGlade

    def single_search(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'single_search' not implemented!"
        event.Skip()

    def close_app(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'close_app' not implemented!"
        event.Skip()

    def open_file(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'open_file' not implemented!"
        event.Skip()

    def save_file(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'save_file' not implemented!"
        event.Skip()

    def adv_search(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'adv_search' not implemented!"
        event.Skip()

    def get_tld(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'get_tld' not implemented!"
        event.Skip()

    def multi_search(self, event):  # wxGlade: MyApp.<event_handler>
        print "Event handler 'multi_search' not implemented!"
        event.Skip()

# end of class MyApp

class AboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("label_1"))
        self.close_about = wx.Button(self, wx.ID_ANY, _("Close"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle(_("About mwhois"))
        self.SetSize((400, 200))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(self.bitmap_1, 0, 0, 0)
        sizer_13.Add(self.label_1, 0, 0, 0)
        sizer_12.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_14.Add(self.close_about, 0, 0, 0)
        sizer_12.Add(sizer_14, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_12)
        self.Layout()
        # end wxGlade

# end of class AboutDialog
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    mwhois_frame = MyApp(None, wx.ID_ANY, "")
    app.SetTopWindow(mwhois_frame)
    mwhois_frame.Show()
    app.MainLoop()