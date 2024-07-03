# sifre=input("Lütfen Şifrenizi Giriniz : ")

# if sifre =="1234":
#     print("Dogru Sifre")
# else:
#     print("Yanlıs Sifre")

# if sifre == "345":
#     print("Kullanıcı Ahmet")
# elif sifre == "123":
#     print("Kullanıcı Osman")
# elif sifre == "741":
#     print("Kullanıcı Eymen")
# else:
#     print("yanlıs sifre")

# yas = int(input("Yasınızı Giriniz : "))

# if yas > 0 and yas <= 10:
#     print("Bir cocuksunuz")
# elif yas > 10 and yas <= 18:
#     print("Bir gençsiniz")
# elif yas > 18 and yas <=50:
#     print("Yetişkinsiniz")
# elif yas > 50 and yas <=100:
#     print("yaslisiniz")
# else:
#     print("Olmeyi unutmusunuz.. ")

# yas = 25
# ad = "Deniz"

# print(type(yas))
# print(type(ad))

puan = 0

cevap1 = input("Türkiye'nin Başkenti neresidir?").upper()
if cevap1 == "ANKARA":
    print("Cevabınız doğru")
    puan = puan + 1

cevap2 = input("Hangi programala dilini öğreniyorsunuz ").lower()
if cevap2 == "python":
    print("Cevabınız doğru!")
    puan = puan + 1

cevap3 = int(input("Türkiye'de kaç il var?"))
if cevap3 == 81:
    print("Cevabınız Doğru")
    puan = puan + 1

print(f"Puanınız : {puan}")