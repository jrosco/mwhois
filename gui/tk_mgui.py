#!/usr/bin/env python

from Tkinter import *
import Tkinter
import tkMessageBox
from mwhois import whois_search

class app_window:

    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()
        
        master.title("Multi Whois Widget")
        master.wm_iconbitmap('../media/icon.ico')
        master["padx"] = 60
        master["pady"] = 20
        
        self.single_label = Label(frame, text="Enter the domain name:")
        self.single_label.pack(side=LEFT)
        #self.single_label.grid(row=1, column=1)
        
        self.single_box = Entry(frame, width=30)
        self.single_box.pack(side=LEFT)

        self.single_button = Button(frame, text="Single Search", command=self.single_command)
        self.single_button.pack(side=LEFT)
        
        self.quit_button = Button(frame, text="QUIT", fg="red", command=frame.quit).pack(side=LEFT)
        
        self.scroll = Tkinter.Scrollbar(master)
        self.text_box = Tkinter.Text(master)
        
        self.scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        self.text_box.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
        self.scroll.config(command=self.text_box.yview)
        self.text_box.config(yscrollcommand=self.scroll.set)

    def single_command(self):
        if self.single_box.get().strip() == "":
            print "Please enter a domain name"
            tkMessageBox.showerror("Multi Whois Widget", "Enter a domain name e.g example.com")
        else:
            print "Running whois single search"
            self.domain = self.single_box.get().strip()
            self.whois = whois_search(self.domain, None, None, None)
            insert = self.whois.single_search()
            self.text_box.delete(1.0, END)
            self.text_box.insert(END, insert)

class mwindow:
    def main(self):
        if __name__ == "__main__":
            root = Tk()
            app = app_window(root)
            root.mainloop()
a=mwindow()
a.main()