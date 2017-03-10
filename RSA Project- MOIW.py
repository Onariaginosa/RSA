from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk

from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk


def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("You typed: ", entrytxt)


def addtolist():
    entrytxt = entry1.get()
    if checkdupe() == False:
        listbox1.insert(END, entrytxt)
        size()
    entry1.delete(0, END)
    
def addtolist2(event):
    entrytxt =entry1.get()
    if checkdupe() == False:
        listbox1.insert(END, entrytxt)
        size()
    entry1.delete(0, END)
    
def clearlist(event):
    listbox1.delete(0, END)
    size()
    
def clearlist2():
    listbox1.delete(0, END)
    size()
    
def checkdupe():
    name = listbox1.get(0, END)
    if entry1.get() in name:
        return True
    else:
        return False

def size():
    label1.config(text=listbox1.size())
    
def openfileR():
    clearlist2()
    f = open("Readme.txt", "r")
    for line in f:

        name = line[0:-1]
        listbox1.insert(END, name)
    f.close()
    size()

def openfileW():
    f = open("Readme.txt", 'w')
    names = listbox1.get(0,END)
    for i in names:    
        f.write(i + "\n") 
    
    f.close()
    

root = Tk() #gives us a blank canvas object to work with
root.title = ("GUI Program")

scrollbar = Scrollbar(root, orient= VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview) 
scrollbar.grid(row=2, column=2, rowspan=10)
T = Text(root, height=20, width=30, yscrollcommand=scrollbar.set)
scrollbar.config(command=T.yview) 
scrollbar.grid(row=0, column=1, rowspan=20, sticky= NS)
T.pack()
T.grid(row=0, column=0, rowspan=10)
T.insert(END, "place public key here \nkill all your friends \nand fake your death\n")



button1 = Button(root, text="button 1", command=addtolist)
button1.grid(row=36, column=36)


scrollbar = Scrollbar(root, orient= VERTICAL)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_command(label="Save", command=openfileW)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes
