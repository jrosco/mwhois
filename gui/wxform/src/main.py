#!/usr/bin/env python

import wx

import mwhois.const as CONST
from mdialog import AboutDialog

import mframe
from controller import SingleSearchThread, MultiSearchThread
from util import WhoisClientUtil
from controller import GUIEvent


# Implementing MyFrame
class MainGUI(mframe.MyFrame):

    def __init__(self, parent):

        mframe.MyFrame.__init__(self, parent)
        self.s_worker = None
        self.m_worker = None
        self.history_select = False
        self.m_textctrl_domain.SetFocus()
        self.dialog = wx.FileDialog(None, style=wx.OPEN)

        """Set icon"""
        ico = wx.Icon('images/mwhois.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        """ App Startup functions"""
        GUIEvent(self).set_tld_list()
        # self.m_listctrl_multi.InsertColumn(0, 'Status', width=150)
        # self.m_listctrl_multi.InsertColumn(1, 'Domain', width=150)
        # self.m_listctrl_multi.InsertColumn(2, 'Creation Date', width=150)
        # self.m_listctrl_multi.InsertColumn(3, 'Expiry Date', width=150)
        # self.m_listctrl_multi.InsertColumn(4, 'Updated Date', width=150)

        """Setup post event Id's"""
        self.SINGLE_SEARCH_EVT_RESULT_ID = wx.NewId()
        self.MULTI_SEARCH_EVT_RESULT_ID = wx.NewId()
        self.SINGLE_SEARCH_EVT_ERROR_ID = wx.NewId()
        self.MULTI_SEARCH_EVT_ERROR_ID = wx.NewId()
        self.HISTORY_DISPLAY_EVT_ID = wx.NewId()
        self.CLEANUP_EVT_ID = wx.NewId()

        """Bind post event functions """
        self.post_whois_search_result(self, self.do_whois_search_result)
        self.post_multi_whois_search_result(self, self.do_whois_multi_search_result)
        self.post_whois_search_error(self, self.do_whois_search_error)
        self.post_multi_whois_search_error(self, self.do_whois_multi_search_error)
        self.post_history_search(self, self.do_display_history_search)
        self.post_cleanup(self, self.do_cleanup)

    """ Post event functions """
    def post_whois_search_result(self, win, func):

        win.Connect(-1, -1, self.SINGLE_SEARCH_EVT_RESULT_ID, func)

    def post_multi_whois_search_result(self, win, func):

        win.Connect(-1, -1, self.MULTI_SEARCH_EVT_RESULT_ID, func)

    def post_whois_search_error(self, win, func):

        win.Connect(-1, -1, self.SINGLE_SEARCH_EVT_ERROR_ID, func)

    def post_multi_whois_search_error(self, win, func):

        win.Connect(-1, -1, self.MULTI_SEARCH_EVT_ERROR_ID, func)

    def post_history_search(self, win, func):

        win.Connect(-1, -1, self.HISTORY_DISPLAY_EVT_ID, func)

    def post_cleanup(self, win, func):

        win.Connect(-1, -1, self.CLEANUP_EVT_ID, func)

    """ UI events """

    def do_whois_search(self, event):

        self.m_button_single_search.Enable(False)
        self.m_textctrl_results.Clear()

        # if not self.m_textctrl_domain.GetValue():
        #     self.m_textctrl_results.SetValue('Please enter a domain')
        #     self.m_button_single_search.Enable(True)

        if not self.s_worker:
            print('self.worker is None')
            self.s_worker = SingleSearchThread(self)
            self.s_worker.start()

    def do_whois_search_result(self, event):

        self.history_select = False
        self.m_textctrl_results.SetValue(event.data[0])
        self.m_textctrl_domain.Clear()
        self.m_combobox_whoisserver.Clear()
        self.m_button_single_search.Enable(True)
        self.m_combobox_whoisserver.SetValue('')

        if event.data[1] == 2:
            self.m_static_is_alive.SetLabel('')

        else:
            if event.data[1] == CONST.DOMAIN_DEAD:
                self.m_static_is_alive.SetForegroundColour('Green')
                self.m_static_is_alive.SetLabel('Available')
            else:
                self.m_static_is_alive.SetForegroundColour(wx.RED)
                self.m_static_is_alive.SetLabel('Not Available')

        self.s_worker = None

    def do_whois_search_error(self, event):

        self.m_textctrl_domain.Clear()
        self.m_combobox_whoisserver.Clear()
        self.m_textctrl_results.SetValue(event.data[0])
        self.m_button_single_search.Enable(True)
        self.s_worker = None

    def do_multi_search(self, event):

        self.m_button_begin.Enable(False)
        self.m_button_stop_multi.Enable(True)
        self.m_listctrl_multi.ClearAll()

        """ Testing """
        self.m_listctrl_multi.InsertColumn(0, 'Status', width=150)
        self.m_listctrl_multi.InsertColumn(1, 'Domain', width=255)
        self.m_listctrl_multi.InsertColumn(2, 'Server', width=255)
        # self.m_listctrl_multi.InsertColumn(2, 'Creation Date', width=150)
        # self.m_listctrl_multi.InsertColumn(3, 'Expiry Date', width=150)
        # self.m_listctrl_multi.InsertColumn(4, 'Updated Date', width=150)

        if not self.m_worker:
            self.m_worker = MultiSearchThread(self)
            self.m_worker.start()

    def do_whois_multi_search_result(self, event):

        if event.data[0] is 1:
            status = 'Not Available'
            status_color = wx.RED
        else:
            status = 'Available'
            status_color = 'Green'

        index = self.m_listctrl_multi.InsertStringItem(0, status)
        self.m_listctrl_multi.SetItemTextColour(index, status_color)
        self.m_listctrl_multi.SetStringItem(index, 1, str(event.data[1]))
        self.m_listctrl_multi.SetStringItem(index, 2, str(event.data[5]))
        # self.m_listctrl_multi.SetStringItem(index, 2, str(event.data[2]))
        # self.m_listctrl_multi.SetStringItem(index, 3, str(event.data[3]))
        # self.m_listctrl_multi.SetStringItem(index, 4, str(event.data[4]))

    def do_whois_multi_search_error(self, event):

        self.do_cleanup()

    def do_history_search(self, event):

        self.history_select = True
        self.do_whois_search(self)

    def do_display_history_search(self, event):

        if self.history_select is False:
            self.m_listbox_history.Append(event.data[0])

    def clear_history(self, event):

        self.m_listbox_history.Clear()

    def do_list_search(self, event):
        #TODO Implement this
        pass

    def do_whois_map(self, event):

        self.m_combobox_whoisserver.Clear()
        get_domain = self.m_textctrl_domain.GetValue()
        whois_map = WhoisClientUtil().map_whois_server(get_domain)

        if whois_map is not None:
            for map_list in whois_map:
                self.m_combobox_whoisserver.Append(map_list)
                self.m_combobox_whoisserver.SetSelection(0)

    def open_file_select(self, event):

        if self.dialog.ShowModal() == wx.ID_OK:
            self.m_textctrl_file.SetValue(self.dialog.GetPath())

    def show_rightclick_menu(self, event):

        #TODO Enable when ready to start testing again
        # if self.m_panel_multi_search is self.FindFocus():
        #     self.m_listctrl_multiOnContextMenu(event)
        # else:
        #     self.m_listbox_historyOnContextMenu(event)
        pass

    def stop_multi_process(self, event):

        self.m_worker.abort()
        self.do_cleanup()

    def do_add_multi_list(self, event):

        multi_list_domain = self.m_text_multi_list.GetValue()

        if len(multi_list_domain):
            self.m_list_multi_list.Append(self.m_text_multi_list.GetValue())

        self.m_text_multi_list.Clear()

    def do_clear_multi_list(self, event):

        self.m_list_multi_list.Clear()

    def do_cleanup(self, *event):

        self.m_button_begin.Enable(True)
        self.m_button_stop_multi.Enable(False)
        self.m_static_mutil_status.SetLabel('Finished')
        self.m_worker = None

    def close_app(self, event):

        wx.Window.Close(self, force=False)

    def on_tld_combo_select(self, event):
        pass

    def on_gtld_combo_select(self, event):
        pass

    def set_dead_only(self, event):
        pass

    def set_sleep(self, event):
        pass

    def create_new_tab(self, event):
        pass

    def do_save_results(self, event):
        pass

    def do_print_results(self, event):
        pass

    def open_about_dialog(self, event):

        about = wx.App(False)
        about_frame = AboutDialog(self, -1, "")
        about.SetTopWindow(about_frame)
        about_frame.CentreOnParent()
        about_frame.Show()
        about.MainLoop()

    def set_preveiw_results(self, event):
        pass
