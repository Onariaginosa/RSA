from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk

from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk


LUT_encryption = dict()
LUT_decryption = dict()

def copye():
    texte = T3.get(1.0,END)

    root2.clipboard_clear()
    root2.clipboard_append(texte)
    clip_text = root.clipboard_get()
    T3.delete('1.0', END)
    T3.insert(END, clip_text)
    
def copyd():
    textd = T4.get(1.0,END)

    root2.clipboard_clear()
    root2.clipboard_append(textd)
    clip_text = root.clipboard_get()
    T4.delete('1.0', END)
    T4.insert(END, clip_text)


def encrypt_message(msg):
    e = int(evalue.get())
    n = int(nvalue.get())
    encrypted_msg = ""
    for letter in msg:
        if letter in LUT_encryption:
            encrypted_msg += LUT_encryption[letter] 
        else :
            numerize = ord(letter) 
            encrypt = pow(numerize, e, n)
            LUT_encryption[letter] = unichr(encrypt)
            encrypted_msg += unichr(encrypt) 
    T3.delete('1.0', END)
    T3.insert(END, encrypted_msg)

def decrypt_message(msg):
    d = int(dvalue.get())
    n = int(nvalue2.get())
    decrypted_msg = ""
    for number in msg:
        if number in LUT_decryption:
            decrypted_msg += LUT_decryption[number]
            print ("joe")
        else :
            numerize = ord(number)
            decrypt = pow(numerize, d, n)
            LUT_encryption[number] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
    T4.delete('1.0', END)
    T4.insert(END, decrypted_msg)
def buttonpress1():
    mesg = T.get(1.0,END)
    encrypt_message(mesg)
    
def buttonpress2():
    msg2 = T2.get(1.0,END)
    decrypt_message(msg2)
    
    
    
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

root2 = Tk()
root2.withdraw()


scrollbar = Scrollbar(root, orient= VERTICAL)
T = Text(root, height=20, width=30, yscrollcommand=scrollbar.set)
scrollbar.config(command=T.yview) 
scrollbar.grid(row=10, column=3, rowspan=5, sticky= NS)
T.pack()
T.grid(row=10, column=1, rowspan=5, columnspan=2)
T.insert(END, "place message here \nkill all your friends \nand fake your death\n")

scrollbar2 = Scrollbar(root, orient= VERTICAL)
T2 = Text(root, height=20, width=30, yscrollcommand=scrollbar2.set)
scrollbar2.config(command=T2.yview) 
scrollbar2.grid(row=10, column=7, rowspan=5, sticky= NS)
T2.pack()
T2.grid(row=10, column=5, rowspan=5, columnspan=2)
T2.insert(END, "place encrypted message here key here \nkill all your friends \nand fake your death\n")

scrollbar3 = Scrollbar(root, orient= VERTICAL)
T3 = Text(root, height=20, width=30, yscrollcommand=scrollbar3.set)
scrollbar3.config(command=T3.yview) 
scrollbar3.grid(row=16, column=3, rowspan=5, sticky= NS)
T3.pack()
T3.grid(row=16, column=1, rowspan=5, columnspan=2)
T3.insert(END, "find encrypted message here \nkill all your friends \nand fake your death\n")

scrollbar4 = Scrollbar(root, orient= VERTICAL)
T4 = Text(root, height=20, width=30, yscrollcommand=scrollbar4.set)
scrollbar4.config(command=T4.yview) 
scrollbar4.grid(row=16, column=7, rowspan=5, sticky= NS)
T4.pack()
T4.grid(row=16, column=5, rowspan=5, columnspan=2)
T4.insert(END, "find decrypted message here key here \nkill all your friends \nand fake your death\n")


elabel = Label(root, text ="e =", anchor=W)
elabel.grid(row=0, column=0,)

nlabel = Label(root, text ="n =", anchor=W)
nlabel.grid(row=1, column=0,)

dlabel = Label(root, text ="d =", anchor=W)
dlabel.grid(row=0, column=4,)

nlabel2 = Label(root, text ="n =", anchor=W)
nlabel2.grid(row=1, column=4,)

dvalue = Entry(root)
dvalue.grid(row=0,column= 5, columnspan=1)


nvalue2 = Entry(root)
nvalue2.grid(row=1,column= 5, columnspan=1)

evalue = Entry(root)
evalue.grid(row=0,column= 1, columnspan=1)

nvalue = Entry(root)
nvalue.grid(row=1,column= 1, columnspan=1)


button1 = Button(root, text="encryption", command=buttonpress1)
button1.grid(row=2, column=1)

button2 = Button(root, text="decryption", command=buttonpress2)
button2.grid(row=2, column=5)

buttonce = Button(root, text="copy encryption", command=copye)
buttonce.grid(row=3, column=1)

buttoncd= Button(root, text="copy decryption", command=copyd)
buttoncd.grid(row=3, column=5)




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
