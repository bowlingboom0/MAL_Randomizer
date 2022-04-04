import tkinter
import api
import random
import pyperclip

root = tkinter.Tk()
root.title("MAL Randomizer")

def randomizer(list):
    chosen = random.choice(list)
    chosen_label.configure(text=f"{chosen}")
    pyperclip.copy(chosen)
    

username_label = tkinter.Label(root, text="MAL Username: ")
username_entry = tkinter.Entry(root)
randomizer_button = tkinter.Button(root, text="Randomize", command=lambda: randomizer(api.get_list(username_entry.get())))
chosen_label = tkinter.Label(root, text="")


username_label.grid(row=0,column=0)
username_entry.grid(row=0,column=1)
randomizer_button.grid(row=1, column=0, columnspan=2)
chosen_label.grid(row=2, column=0, columnspan=2)

root.mainloop()