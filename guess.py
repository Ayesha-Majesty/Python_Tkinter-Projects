from tkinter import *
from random import randint

root=Tk()
root.title('GUESS THE NUMBER')
root.geometry("500x500")

num_label = Label(root,text="Pick a number \n from 1 to 10!", font=("Brush Script MT", 32))
num_label.pack(pady=20)


# DEFINING FUNCTIONALITIES
def guesser():
    if guess_box.get().isdigit():
        num_label.config(text="Pick a number \n from 1 to 10!")

        # find out how far away our pick was from actual number
        dif = abs(num - int(guess_box.get())) 
        
        # check to see if correct
        if int(guess_box.get()) == num:
            bc= "SystemButtonFace"
            num_label.config(text="CORRECT!")
        elif dif == 5:
            # white
            bc = "WHITE"

        elif dif < 5:
            # red
            bc = f'#ff{dif}{dif}{dif}{dif}'
             
        else:
            # blue
            bc=  f'#{dif}{dif}{dif}{dif}ff'

        root.config(bg = bc)
        num_label.config(bg = bc)

    else:
        guess_box.delete(0,END)
        num_label.config(text="Hey! Thats not a Number!")


def rando():
    global num
    num= randint(1,10)
    # Clear the guess box
    guess_box.delete(0,END)
    
    root.config(bg = "SystemButtonFace")
    num_label.config(bg = "SystemButtonFace", text="Pick a number \n from 1 to 10!")


guess_box = Entry(root, font=("Helvetica", 80), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text="Submit", command= guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="New Number", command= rando)
rand_button.pack(pady=20)


# generate a random number on start
rando()
root.mainloop()
