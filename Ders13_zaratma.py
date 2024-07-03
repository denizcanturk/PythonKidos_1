import tkinter as tk
import random as rd
import time as t

pencere = tk.Tk()
pencere.title("Şanslı Zarlar")
pencere.geometry("500x300")


zarlar = ["⚀","⚁","⚂","⚃","⚄","⚅"]

def zarAt(zarlar):
    donmeZamani = rd.randint(1,100)
    for i in range(donmeZamani):
        lblZar.configure(text="{}{}".format( rd.choice(zarlar), rd.choice(zarlar) ) )
        lblZar.pack()
        zamaniYavaslat = ((i+1)/donmeZamani)/4
        t.sleep(zamaniYavaslat)
        pencere.update()

btnZarat = tk.Button(pencere, text="ZAR AT", font=30, bg="red",fg="white", \
                     width=20,height=2, command=lambda:zarAt(zarlar))
btnZarat.pack(pady=10)

lblZar = tk.Label(pencere, text = "", font=("Arial",150))
lblZar.pack()

pencere.mainloop()
