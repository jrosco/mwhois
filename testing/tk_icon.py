# changing the default icon in Tkinter programs

from Tkinter import *

# create the form and a label
form1 = Tk()
lbl1 = Label(form1, text='Changing the Tk icon is very easy!')
lbl1.pack(expand=YES, fill=BOTH)

# change the form/frame icon, use an icon file you have ...
form1.wm_iconbitmap('C:/Python25/py.ico')
form1.wm_title('New Icon')

# run it ...
form1.mainloop()