import tkinter as tk
from time import strftime

renk = True
renkler = ["red", "blue", "purple", "white", "green", "pink","yellow", "violet", "gray", "brown"]
counter = 0

pencere = tk.Tk()
pencere.title("Benim Saatim")
pencere.geometry("400x100")
pencere.configure(background="black")

def zaman():
    global counter
    # global renk
    # if renk == True:
    #     lblEtiket.configure(background="blue")
    #     renk=False
    # else:
    #     lblEtiket.configure(background="red")
    #     renk=True
    
    lblEtiket.configure(background=renkler[counter], foreground=renkler[counter-2])
    counter+=1
    if counter >= len(renkler):
        counter = 0
    zmn = strftime("%H:%M:%S %p")
    lblEtiket.configure(text=zmn)
    lblEtiket.after(100, zaman)

lblEtiket = tk.Label(pencere, text="saat",font=("calibri",50,"bold"), \
    background = "red", foreground="white")

lblEtiket.pack(anchor="center")

zaman()
pencere.mainloop()