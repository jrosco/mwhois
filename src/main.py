#!/usr/bin/env python

from Tkinter import *
import tkMessageBox
from multi_whois import whois_search

class app_window:

    def __init__(self, master):
        
        global single_box
        
        frame = Frame(master)
        frame.pack()
        
        master.title("Multi Whois Widget")
        master["padx"] = 60
        master["pady"] = 20
        
        single_label = Label(frame)
        single_label["text"] = "Enter the domain name:"
        single_label.pack(side=LEFT)
        
        single_box = Entry(frame)
        single_box["width"] = 30
        single_box.pack(side=LEFT)

        self.single = Button(frame, text="Single Search", command=self.single_command)
        self.single.pack(side=LEFT)
        
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

    def single_command(self):
        if single_box.get().strip() == "":
            print "Please enter a domain name"
            tkMessageBox.showerror("Tkinter Entry Widget", "Enter a domain name e.g example.com")
        else:
            print "Running whois single search"
            domain = single_box.get().strip()
            self.whois = whois_search(domain, None, None, None)
            self.whois.single_search()


if __name__ == "__main__":
    root = Tk()
    app = app_window(root)
    root.mainloop()
