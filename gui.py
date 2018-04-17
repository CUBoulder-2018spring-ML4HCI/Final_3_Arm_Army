#!/usr/bin/python

from tkinter import *
import pickle

root = Tk()
root.geometry("600x400")
root.title("Gesture Trainer")

OPTIONS = [
"Get Cereal",
"Bring Spoon to Face",
"Stir"
] #etc

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

def ok():
    print ("Gesture to train is:" + variable.get())

def Train():
	text_contents = text.get()
	listbox.insert(END, text_contents)
	text.delete(0,END)

def send_osc(event):
    global running
    print("sending...")
    running = True

def stop_osc(event):
    global running
    running = False
    print("stopping...")

textframe = Frame(root)
listframe = Frame(root)

train_button = Button(textframe, text="Train", command = Train)

button = Button(root, text="OK", command=ok)

test_button= Button(root, text = "Training Mode")
test_button.pack(side=RIGHT)
test_button.bind('<ButtonPress-1>',send_osc)
test_button.bind('<ButtonRelease-1>',stop_osc)

train_button.pack(side=LEFT)

listframe.pack(fill=BOTH, expand=1)

button.pack()

try:
	f = file("notes.db", "rb")
	notes = pickle.load(f)
	for item in notes:
		listbox.insert(END,item)
	f.close()
except:
	pass

root.mainloop()
