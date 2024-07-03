import tkinter as tk
genislik = 600
yukseklik = 100


def yaziyiKaydir():
    canva.move(text, -1, 0)
    canva.move(text2, 1, 0)
    x, _ = canva.coords(text)
    x2, _ = canva.coords(text2)
    if x < -500:
        canva.coords(text, 600,25)
    if x2 > 600:
        canva.coords(text2,-100,75)
    pencere.after(30,yaziyiKaydir)



pencere = tk.Tk()
pencere.title("Kayan Yazi")
pencere.geometry(f"{genislik}x{yukseklik}")

canva = tk.Canvas(pencere, width = genislik, height=yukseklik, bg="black")
canva.pack()

text = canva.create_text(600, 25, \
                         text="Yalnız taştan duvar olmaz, bunu yaz bir yere",\
                         font=("Helvetica", 20),\
                         fill="turquoise")

text2 = canva.create_text(-100, 75, \
                         text="Dum tıs tıs tıs Dum tıs tıs tıs",\
                         font=("Helvetica", 20),\
                         fill="turquoise")

yaziyiKaydir()
pencere.mainloop()