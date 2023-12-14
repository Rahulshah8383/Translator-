from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.config(background="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    Label1.config(text=c)
    Label2.config(text=c1) 
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# icon
image_icon = PhotoImage(file="image.png")
root.iconphoto(False, image_icon)

# arrow
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

language = LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# first combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

Label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
Label1.place(x=10, y=50)

# second combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

Label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
Label2.place(x=620, y=50)

# first frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

Scrollbar1 = Scrollbar(f1)
Scrollbar1.pack(side="right", fill='y')

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

# second frame
f2 = Frame(root, bg="Black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(f2)
Scrollbar2.pack(side="right", fill='y')

Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# translate button
translate = Button(root, text="Translate", font=("Robote", 15), activebackground="white", cursor="hand2"
                   , bd=1, width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=476, y=250)

label_change()
root.mainloop()