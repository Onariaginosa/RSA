from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk

from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk

def encrypt_message(msg):
    for letter in msg:
        numerize = ord(letter)
        encrypt = pow(numerize, e, n)
        encrypted_msg += unichr(encrypt) 
    return encrypted_msg

def buttonpress1():
    entrytxt = T.get(1.0,END)
    print entrytxt
    tkMessageBox.showinfo("You typed: ", entrytxt)
    encrypt_message(entrytxt)
    
def decrypt_message(msg):
    for number in msg:
       numerize = ord(number)
       decrypt = pow(numerize, d, n)
       decrypted_msg += unichr(decrypt)
    return decrypted_msg
    
def buttonpress2():
    entrytxt2 = T.get(1.0,END)
    print entrytxt2
    tkMessageBox.showinfo("You typed: ", entrytxt)
    decrypt_message(entrytxt2)
    
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
T = Text(root, height=20, width=30, yscrollcommand=scrollbar.set)
scrollbar.config(command=T.yview) 
scrollbar.grid(row=10, column=2, rowspan=20, sticky= NS)
T.pack()
T.grid(row=10, column=0, rowspan=10, columnspan=2)
T.insert(END, "place public key here \nkill all your friends \nand fake your death\n")

scrollbar2 = Scrollbar(root, orient= VERTICAL)
T2 = Text(root, height=20, width=30, yscrollcommand=scrollbar2.set)
scrollbar2.config(command=T2.yview) 
scrollbar2.grid(row=10, column=6, rowspan=20, sticky= NS)
T2.pack()
T2.grid(row=10, column=4, rowspan=10, columnspan=2)
T2.insert(END, "place private key here \nkill all your friends \nand fake your death\n")

entry1 = Entry(root)
entry1.grid(row=0,column= 0, columnspan=1)
entry1.bind("<Return>", buttonpress1)

entry2 = Entry(root)
entry2.grid(row=1,column= 0, columnspan=1)
entry2.bind("<Return>", buttonpress1)

button1 = Button(root, text="encryption", command=buttonpress1)
button1.grid(row=2, column=0)

button2 = Button(root, text="decryption", command=buttonpress2)
button2.grid(row=2, column=4)

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
