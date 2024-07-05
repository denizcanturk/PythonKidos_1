import tkinter as tk
import pyttsx3 as p

konusucu = p.init()

def konus():
    konusucu.setProperty("rate", 120)
    konusucu.say(enGiris.get())
    konusucu.runAndWait()
    konusucu.stop()

pencere = tk.Tk()
pencere.title("Konus Bakalım")
pencere.geometry("300x50")

lblEtiket = tk.Label(pencere, text = "Metin", font=30 )
lblEtiket.pack(side=tk.LEFT, padx=5)

enGiris = tk.Entry(pencere, font = 30, width=15, bd=0)
enGiris.pack(side=tk.LEFT, padx=5)

btnDugme = tk.Button(pencere, text="Konus", bg="red", fg="white", bd=5, command=konus)
btnDugme.pack(side=tk.LEFT, padx=5)

pencere.mainloop()