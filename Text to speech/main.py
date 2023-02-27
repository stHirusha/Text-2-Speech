import pyttsx3
from customtkinter import *
from tkinter import messagebox

engine = pyttsx3.init()

def convert():
    global male_checked, female_checked
    if male_checked.get() == 1 and female_checked.get() == 0:
        male()
    elif male_checked.get() == 0 and female_checked.get() == 1:
        female()
    elif male_checked.get() == 0 and female_checked.get() == 0:
        male()
    else:
        messagebox.showerror("Error","Please\nOnly check one box")


def male():
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[0].id)
   engine.say(textvar.get())
   engine.runAndWait()
   engine.stop()  # <-- moved this line here

def female():
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)
   engine.say(textvar.get())
   engine.runAndWait()
   engine.stop()  # <-- moved this line here


root = CTk()
root.title("Text-to-Speech")
root.geometry("400x200+10+10")
root.resizable(False, False)

set_appearance_mode("dark")
set_default_color_theme("green")

textvar = StringVar()

frame = CTkFrame(root, border_width=3)
frame.pack(fill="both", expand=True, padx=10, pady=10)

label = CTkLabel(frame, text="Text to Speech", font=("Arial", 20), bg_color="transparent")
label.pack(side=TOP, anchor="nw", padx=10, pady=5)

entry = CTkEntry(frame, textvariable=textvar, height=90)
entry.pack(fill="x", padx=10)

btn = CTkButton(frame, text="Convert", font=("Arial", 20), command=convert)
btn.pack(side="left", padx=10, pady=10)

male_checked = IntVar()
female_checked = IntVar()

btn1 = CTkCheckBox(frame, text="Male", border_width=2, variable=male_checked)
btn1.place(x=170, y=140)
btn2 = CTkCheckBox(frame, text="Female", border_width=2, variable=female_checked)
btn2.place(x=270, y=140)

root.mainloop()
