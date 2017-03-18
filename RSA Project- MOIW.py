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
    tkMessageBox.showinfo("Encryption Copied", "You have copied the encrypted text")
    
def copyd():
    textd = T4.get(1.0,END)

    root2.clipboard_clear()
    root2.clipboard_append(textd)
    clip_text = root.clipboard_get()
    T4.delete('1.0', END)
    T4.insert(END, clip_text)
    tkMessageBox.showinfo("Decryption Copied", "You have copied the decrypted text")


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
    LUT_encryption.clear()
    T3.delete('1.0', END)
    T3.insert(END, encrypted_msg)

def decrypt_message(msg):
    d = int(dvalue.get())
    n = int(nvalue2.get())
    decrypted_msg = ""
    for number in msg:
        if number in LUT_decryption:
            decrypted_msg += LUT_decryption[number]
        else :
            numerize = ord(number)
            decrypt = pow(numerize, d, n)
            LUT_decryption[number] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
    LUT_decryption.clear()
    T4.delete('1.0', END)
    T4.insert(END, decrypted_msg)
def buttonpress1():
    mesg = T.get(1.0,END)
    encrypt_message(mesg)
    
def buttonpress2():
    msg2 = T2.get(1.0,END)
    decrypt_message(msg2)
    
def clear():
    evalue.delete(0, END)
    nvalue.delete(0, END)  
    dvalue.delete(0, END)
    nvalue2.delete(0, END)
    T.delete('1.0', END)
    T2.delete('1.0', END)
    T3.delete('1.0', END)
    T4.delete('1.0', END)
def openfileR():
    E = open("E.txt", "r")
    for line in E:
        name = line[0:-1]
        evalue.delete(0, END)
        evalue.insert(END, name)
    E.close()
    N = open("N.txt", "r")
    for line in N:
        name = line[0:-1]
        nvalue.delete(0, END)
        nvalue.insert(END, name)
    N.close()
    D = open("D.txt", "r")
    for line in D:
        name = line[0:-1]
        dvalue.delete(0, END)
        dvalue.insert(END, name)
    D.close()
    N2 = open("N2.txt", "r")
    for line in N2:
        name = line[0:-1]
        nvalue2.delete(0, END)
        nvalue2.insert(END, name)
    N2.close()
    
    Te = open("Textbox1.txt", "r")
    i = Te.read()
    T.delete('1.0', END)
    T.insert(END,i)
    Te.close()
    
    Te2 = open("Textbox2.txt", "r")
    i = Te2.read()
    T2.delete('1.0', END)
    T2.insert(END, i)
    Te2.close()
    
    Te3 = open("Textbox3.txt", "r")
    i = Te3.read()
    T3.delete('1.0', END)
    T3.insert(END, i)
    Te3.close()
    
    Te4 = open("Textbox4.txt", "r")
    i = Te4.read()
    T4.delete('1.0', END)
    T4.insert(END, i)
    Te4.close()


def openfileW():
    E = open("E.txt", "w")
    names =evalue.get()
    E.write(names + "\n")
    E.close()
    
    N = open("N.txt", "w")
    names =nvalue.get()
    N.write(names + "\n")
    N.close()
    
    D = open("D.txt", "w")
    names =dvalue.get()
    D.write(names + "\n")
    D.close()
    
    N2 = open("N2.txt", "w")
    names =nvalue2.get()
    N2.write(names + "\n")
    N2.close()
    
    Te = open("Textbox1.txt", "w")
    i = T.get(1.0,END)
    
    Te.write(i)
    Te.close()
    
    Te2 = open("Textbox2.txt", "w")
    i2 = T2.get(1.0,END)
    Te2.write(i2)
    Te2.close()
    
    Te3 = open("Textbox3.txt", "w")
    i3 = T3.get(1.0,END)
    Te3.write(i3)
    Te3.close()
    
    Te4 = open("Textbox4.txt", "w")
    i4 = T4.get(1.0,END)
    Te4.write(i4)
    Te4.close()
    tkMessageBox.showinfo("Saved", "You have successfully saved your values.")

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
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)
menubar.add_cascade(label="File", menu=filemenu)

menubar2 = Menu(root)
othermenu = Menu(menubar2, tearoff=0)
othermenu.add_command(label="Exit", command=root.quit)
othermenu.add_separator()
othermenu.add_command(label="Clear all", command= clear)
menubar.add_cascade(label="Other", menu=othermenu)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes
