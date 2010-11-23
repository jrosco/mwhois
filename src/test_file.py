
import wx

class get_line():
     
    def line(self, file, object):
        
        self.textbox = object
        self.file = file
        for self.line in open(self.file,'r').readlines():
            self.textbox.AppendText(self.line)