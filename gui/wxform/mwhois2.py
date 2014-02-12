# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Multi Whois", pos = wx.Point( -1,-1 ), size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1024,768 ), wx.Size( -1,-1 ) )
		
		self.m_menubar_top = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_newtab = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"New Tab", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_newtab )
		
		self.m_menuItem_save = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_save )
		
		self.m_menuItem_print = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Print", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_print )
		
		self.m_menuItem_close = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_close )
		
		self.m_menubar_top.Append( self.m_menu_file, u"File" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menuItem_about )
		
		self.m_menubar_top.Append( self.m_menu_help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar_top )
		
		bSizerMainWindow = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebooktab = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_single_search = wx.Panel( self.m_notebooktab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		gSizerSearchArea = wx.GridSizer( 0, 3, 0, 0 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextDomainLabel = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"Domain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextDomainLabel.Wrap( -1 )
		bSizer4.Add( self.m_staticTextDomainLabel, 0, wx.ALL, 5 )
		
		self.m_textctrl_domain = wx.TextCtrl( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 255,-1 ), 0 )
		self.m_textctrl_domain.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_textctrl_domain, 0, wx.ALL, 5 )
		
		
		gSizerSearchArea.Add( bSizer4, 0, 0, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextWhoisServerLabel = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"Choose Whois Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextWhoisServerLabel.Wrap( -1 )
		bSizer7.Add( self.m_staticTextWhoisServerLabel, 0, wx.ALL, 5 )
		
		m_combobox_whoisserverChoices = [ u"whois.server.net", u"whois.server.org", u"whois.server.edu", u"whois.server.guru", u"whois.server.com" ]
		self.m_combobox_whoisserver = wx.ComboBox( self.m_panel_single_search, wx.ID_ANY, u"whois.server.guru", wx.DefaultPosition, wx.Size( 255,-1 ), m_combobox_whoisserverChoices, wx.CB_READONLY )
		self.m_combobox_whoisserver.SetSelection( 3 )
		self.m_combobox_whoisserver.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_combobox_whoisserver, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerSearchArea.Add( bSizer7, 0, 0, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextSearchHidden = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSearchHidden.Wrap( -1 )
		bSizer8.Add( self.m_staticTextSearchHidden, 0, wx.ALL, 5 )
		
		self.m_button_single_search = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer8.Add( self.m_button_single_search, 0, wx.ALIGN_RIGHT, 5 )
		
		
		gSizerSearchArea.Add( bSizer8, 0, 0, 5 )
		
		
		bSizer3.Add( gSizerSearchArea, 0, wx.EXPAND, 5 )
		
		gSizerResultsArea = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9.SetMinSize( wx.Size( 600,-1 ) ) 
		self.m_staticText6 = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"Results", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer9.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textctrl_results = wx.TextCtrl( self.m_panel_single_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer9.Add( self.m_textctrl_results, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerResultsArea.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11.SetMinSize( wx.Size( 200,-1 ) ) 
		self.m_staticText7 = wx.StaticText( self.m_panel_single_search, wx.ID_ANY, u"History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer11.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_listbox_historyChoices = []
		self.m_listbox_history = wx.ListBox( self.m_panel_single_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_listbox_historyChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		self.m_listbox_history.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_listbox_history, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizerResultsArea.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( gSizerResultsArea, 1, wx.EXPAND, 5 )
		
		gSizerBottomButtons = wx.GridSizer( 0, 3, 1, 1 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button_print1 = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button_print1, 0, wx.ALL, 5 )
		
		
		gSizerBottomButtons.Add( bSizer18, 0, 0, 5 )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button_save1 = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.m_button_save1, 0, wx.ALL, 5 )
		
		
		gSizerBottomButtons.Add( bSizer191, 0, 0, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button_quit1 = wx.Button( self.m_panel_single_search, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button_quit1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gSizerBottomButtons.Add( bSizer20, 0, 0, 5 )
		
		
		bSizer3.Add( gSizerBottomButtons, 0, 0, 5 )
		
		
		self.m_panel_single_search.SetSizer( bSizer3 )
		self.m_panel_single_search.Layout()
		bSizer3.Fit( self.m_panel_single_search )
		self.m_notebooktab.AddPage( self.m_panel_single_search, u"Single Search", False )
		self.m_panel_multi_search = wx.Panel( self.m_notebooktab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText71 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Wordlist", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer24.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.m_textctrl_file = wx.TextCtrl( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 255,-1 ), 0 )
		bSizer24.Add( self.m_textctrl_file, 0, wx.ALL, 5 )
		
		self.m_button_open = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button_open, 0, wx.ALL, 5 )
		
		m_combo_tldChoices = []
		self.m_combo_tld = wx.ComboBox( self.m_panel_multi_search, wx.ID_ANY, u"TLD", wx.DefaultPosition, wx.DefaultSize, m_combo_tldChoices, 0 )
		bSizer24.Add( self.m_combo_tld, 0, wx.ALL, 5 )
		
		m_combo_cctldChoices = []
		self.m_combo_cctld = wx.ComboBox( self.m_panel_multi_search, wx.ID_ANY, u"ccTLD", wx.DefaultPosition, wx.DefaultSize, m_combo_cctldChoices, 0 )
		bSizer24.Add( self.m_combo_cctld, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer25.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkbox_dead = wx.CheckBox( self.m_panel_multi_search, wx.ID_ANY, u"Dead Only", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkbox_dead.SetToolTipString( u"Show only domains that are available" )
		
		bSizer26.Add( self.m_checkbox_dead, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel_multi_search, wx.ID_ANY, u"Sleep", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer26.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_textctrl_sleep = wx.TextCtrl( self.m_panel_multi_search, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_textctrl_sleep.SetToolTipString( u"Number of seconds to sleep between whois queries" )
		
		bSizer26.Add( self.m_textctrl_sleep, 0, wx.ALL, 5 )
		
		self.m_button_begin = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Begin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_begin.SetToolTipString( u"Start searching" )
		
		bSizer26.Add( self.m_button_begin, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer26, 0, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listctrl_multi = wx.ListCtrl( self.m_panel_multi_search, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON )
		bSizer27.Add( self.m_listctrl_multi, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button_print2 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_print2, 0, wx.ALL, 5 )
		
		self.m_button_save2 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_save2, 0, wx.ALL, 5 )
		
		self.m_button_quit2 = wx.Button( self.m_panel_multi_search, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button_quit2, 0, wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer27, 1, wx.EXPAND, 5 )
		
		
		self.m_panel_multi_search.SetSizer( bSizer19 )
		self.m_panel_multi_search.Layout()
		bSizer19.Fit( self.m_panel_multi_search )
		self.m_notebooktab.AddPage( self.m_panel_multi_search, u"Multi Search", True )
		
		bSizerMainWindow.Add( self.m_notebooktab, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerMainWindow )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.create_new_tab, id = self.m_menuItem_newtab.GetId() )
		self.Bind( wx.EVT_MENU, self.do_save_results, id = self.m_menuItem_save.GetId() )
		self.Bind( wx.EVT_MENU, self.do_print_results, id = self.m_menuItem_print.GetId() )
		self.Bind( wx.EVT_MENU, self.close_app, id = self.m_menuItem_close.GetId() )
		self.Bind( wx.EVT_MENU, self.open_about_dialog, id = self.m_menuItem_about.GetId() )
		self.m_notebooktab.Bind( wx.EVT_SET_FOCUS, self.set_preveiw_results )
		self.m_textctrl_domain.Bind( wx.EVT_TEXT_ENTER, self.do_whois_search )
		self.m_button_single_search.Bind( wx.EVT_BUTTON, self.do_whois_search )
		self.m_button_print1.Bind( wx.EVT_BUTTON, self.do_print_results )
		self.m_button_save1.Bind( wx.EVT_BUTTON, self.do_save_results )
		self.m_button_quit1.Bind( wx.EVT_BUTTON, self.close_app )
		self.m_button_open.Bind( wx.EVT_BUTTON, self.open_file_select )
		self.m_checkbox_dead.Bind( wx.EVT_CHECKBOX, self.set_dead_only )
		self.m_textctrl_sleep.Bind( wx.EVT_TEXT, self.set_sleep )
		self.m_button_begin.Bind( wx.EVT_BUTTON, self.do_multi_search )
		self.m_button_print2.Bind( wx.EVT_BUTTON, self.do_print_results )
		self.m_button_save2.Bind( wx.EVT_BUTTON, self.do_save_results )
		self.m_button_quit2.Bind( wx.EVT_BUTTON, self.close_app )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def create_new_tab( self, event ):
		event.Skip()
	
	def do_save_results( self, event ):
		event.Skip()
	
	def do_print_results( self, event ):
		event.Skip()
	
	def close_app( self, event ):
		event.Skip()
	
	def open_about_dialog( self, event ):
		event.Skip()
	
	def set_preveiw_results( self, event ):
		event.Skip()
	
	def do_whois_search( self, event ):
		event.Skip()
	
	def open_file_select( self, event ):
		event.Skip()
	
	def set_dead_only( self, event ):
		event.Skip()
	
	def set_sleep( self, event ):
		event.Skip()
	
	def do_multi_search( self, event ):
		event.Skip()
	
