import random

bilgisayar = random.randint(1,10)


while True:
    kullanici = int(input("Bir sayi giriniz : "))
    if bilgisayar == kullanici:
        print("Doğru Tahmin")
        break
    else:
        print(3*" Bilmedikiiiii")