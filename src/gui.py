#!/usr/bin/env python

from Tkinter import *
import Tkinter
import tkMessageBox
from multi_whois import whois_search

class app_window:

    def __init__(self, master):
        
        global single_box
        global text_box
        
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
        
        scroll = Tkinter.Scrollbar(master)
        text_box = Tkinter.Text(master)
        
        scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        text_box.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
        scroll.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll.set)

    def single_command(self):
        if single_box.get().strip() == "":
            print "Please enter a domain name"
            tkMessageBox.showerror("Tkinter Entry Widget", "Enter a domain name e.g example.com")
        else:
            print "Running whois single search"
            domain = single_box.get().strip()
            self.whois = whois_search(domain, None, None, None)
            insert = self.whois.single_search()
            text_box.delete(1.0, END)
            text_box.insert(END, insert)


if __name__ == "__main__":
    root = Tk()
    app = app_window(root)
    root.mainloop()
