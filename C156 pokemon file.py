from tkinter import *
from PIL import ImageTk, Image
import random
root=Tk()

root.title("Endless Dice Game")
root.geometry("600x650")

root.configure(background="sky blue")

img1=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
img2=ImageTk.PhotoImage(Image.open("ratata.jpg"))
img3=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
img4=ImageTk.PhotoImage(Image.open("persion.jpg"))
img5=ImageTk.PhotoImage(Image.open("paras.jpg"))
img6=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
img7=ImageTk.PhotoImage(Image.open("meowth.jpg"))
img8=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
img9=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
img10=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
img11=ImageTk.PhotoImage(Image.open("charmender.jpg"))
img12=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))

player_1 = Label(root, text="Player 1", fg="black", bg="cyan")
player_1.place(relx = 0.1, rely = 0.3, anchor=CENTER)

player_2 = Label(root, text="Player 2", fg="black", bg="cyan")
player_2.place(relx = 0.9, rely = 0.3, anchor=CENTER)

player1_score_label = Label(root, bg="blue", fg="black")
player1_score_label.place(relx = 0.1, rely = 0.4, anchor=CENTER)

player2_score_label = Label(root, bg="blue", fg="black")
player2_score_label.place(relx = 0.9, rely = 0.4, anchor=CENTER)

random_dice_label = Label(root, bg="lime", fg="white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor=CENTER)

root.mainloop()