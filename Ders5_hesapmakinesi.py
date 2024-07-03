import tkinter as tk

def hesapla(event=None):
    islem = giris.get()
    sonuc = eval(islem)
    giris.insert(tk.END, " = " + str(sonuc))

def ekranTemizle(event=None):
    giris.delete(0,tk.END)

pencere = tk.Tk()
pencere.title("Hesap Makinesi")

ekranGenisligi = pencere.winfo_screenwidth()
ekranYuksekligi = pencere.winfo_screenheight()

pencereGenisligi = 360
pencereYuksekligi = 50

x = int((ekranGenisligi / 2) - (pencereGenisligi/2))
y = int((ekranYuksekligi / 2) - (pencereYuksekligi / 2))
print(x, y)

pencere.geometry(f"{pencereGenisligi}x{pencereYuksekligi}+{x}+{y}")

etiket = tk.Label(pencere, text="İşlem", font=30)
etiket.pack(side=tk.LEFT, padx=5)

giris = tk.Entry(pencere,font=30, width=15,bd=0)
giris.pack(side= tk.LEFT, padx=5)

dugme = tk.Button(pencere, text="Hesapla", command=hesapla)
dugme.pack(side=tk.LEFT, padx=5)

giris.bind('<Return>', hesapla)
#Burayı girmeyi unutmuşum...:(
giris.bind('<Escape>',ekranTemizle)

temizle = tk.Button(pencere, text="Temizle", command=ekranTemizle)
temizle.pack(side=tk.LEFT, padx=5)


pencere.mainloop()
