import tkinter as tk
import pyttsx3 as p

kns = p.init()

def konus():
    kns.say(giris.get())
    kns.runAndWait()
    kns.stop()

pencere = tk.Tk()
pencere.title("Konus Bakalım")
pencere.geometry("300x50")

etiket = tk.Label(pencere, text="Metin", font = 30)
etiket.pack(side=tk.LEFT, padx=5)

giris = tk.Entry(pencere, width=15, font = 30, bd=0)
giris.pack(side=tk.LEFT, padx=5)

dugme = tk.Button(pencere, text="Konus", bg="red", fg="white", command=konus)
dugme.pack(side=tk.LEFT, padx=5)

pencere.mainloop()