import tkinter as tk
import random as rd

pencere = tk.Tk()
pencere.title("Taş Kağıt Makas Oyunu")
pencere.geometry("400x200")

oyuncuSkoru= 0
bilgisayarSkoru = 0
berabereSkoru = 0


def oynat(secim):
    sonuc=""
    global oyuncuSkoru, bilgisayarSkoru,berabereSkoru
    secimler = ["Tas", "Kagit", "Makas"]
    bilgisayar = rd.choice(secimler)

    if secim ==bilgisayar:
        sonuc = "Berabere"
        berabereSkoru +=1

    elif (secim == "Tas" and bilgisayar == "Kagit") or \
         (secim == "Kagit" and bilgisayar == "Makas") or \
         (secim == "Makas" and bilgisayar == "Tas"):
        sonuc = "Kaybettiniz"
        bilgisayarSkoru +=1

    else:
        sonuc = "Kazandiniz"
        oyuncuSkoru+=1

    skorDurumu = f"Siz : {oyuncuSkoru}, Bilgisayar : {bilgisayarSkoru}, Berabere : {berabereSkoru}"
    guncelDurum = f"Siz : {secim}, Bilgisayar : {bilgisayar}, Sonuc: {sonuc}"
    skorEtiket.configure(text=skorDurumu)
    oyunEtiket.configure(text=guncelDurum)

skorEtiket = tk.Label(pencere,text="Siz : 0, Bilgisayar = 0, Berabere = 0", \
                      font=("Arial",14))
skorEtiket.pack(pady=10)

oyunEtiket = tk.Label(pencere,text = "Siz : Tas, Bilgisayar : Kagit, Sonuc : Kazandınız!")
oyunEtiket.pack(pady=10)


btnTas = tk.Button(pencere, text="\u270A", width = 2, font = ("Arial",40), \
                    command=lambda:oynat("Tas"))
btnTas.pack(side=tk.LEFT, padx=10)

btnKagit = tk.Button(pencere, text="\u270B", width = 2, font = ("Arial",40) ,\
                     command=lambda:oynat("Kagit"))
btnKagit.pack(side=tk.LEFT, padx=10)

btnMakas = tk.Button(pencere, text="\u2704", width = 2, font = ("Arial",40) , \
                     command=lambda:oynat("Makas"))
btnMakas.pack(side=tk.LEFT, padx=10)



pencere.mainloop()