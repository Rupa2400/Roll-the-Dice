import tkinter
from PIL import Image, ImageTk
import random

root=tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice!')
root.configure(bg = '#ffc4f4')

l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text = 'Hello Everyone', fg = "#003cff", bg = "#defffc", font = "Algerian 17 bold italic")
l1.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image = image1)
label1.image = image1

label1.pack(expand = True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

button = tkinter.Button(root, text = 'Roll the Dice', fg = 'blue', command= rolling_dice)
button.pack(expand = True)

root.mainloop()
