# kitaplik = ["Tarih", "Matematik", "Fizik", "Türkçe","Bilişim","Kimya","Coğrafya"]

# print(kitaplik)

# # for kitap in kitaplik:
# #     print(kitap)

# print(kitaplik[3])

# sinif = []

# sinif.append("Deniz")
# sinif.append("Ayşe")
# sinif.append("Zehra")
# sinif.append("Aras")

# print(sinif)

# for ogrenci in sinif:
#     print(ogrenci)

# for i in range(10):
#     if i%2==1:
#         print(i, "Tek Sayıdır")

# for i in range(10):
#     if i%3==0:
#         print(i, "Üç ün katıdır")


#-+-------------------------------------

#TODO : 
# 1 CEVEP a İNT GİRMEME GEREK VAR MI?
# 2 SECENEK 2 İÇİN EĞER LİSTE BOŞSA SECENEĞİ EKLENMELİ
# 3 SECENEK 3 İÇİN EĞER LİSTE BOŞSA İKAZ VERSİN SEÇENEĞİ
secenekler = [1,2,3,4]
sinif = []
while True:
    menu = """
        ---- MENU ----
        1. Ögrenci Ekle
        2. Öğrenci Sil
        3. Öğrenci Listele
        4. Programdan Çık
        > """

    cevap = int(input(menu))

    if cevap not in secenekler:
        print("Geçerli bir seçenek giriniz")
    else:
        if cevap == 1:
            ogrenci = input("Ogrenci Adi Giriniz :")
            sinif.append(ogrenci)
        if cevap ==2 :
            if len(sinif) == 0:
                print("Sınıfta silinecek öğrenci yok")
                continue

            ogrenci = input("Ogrenci Adi Giriniz :")
            ogrenciSayisi = sinif.count(ogrenci)
            if ogrenciSayisi == 0:
                print("Ogrenci Mevcut Değil")
            else:
                sinif.remove(ogrenci)
                print("Ogrenci Siniftan cıkarıldı")

        if cevap == 3:
            if len(sinif) == 0:
                print("Sınıfta henüz öğrenci yok!")
            else:
                for ogrenci in sinif:
                    print(ogrenci)
        if cevap == 4:
            print("Görüşmek üzere.")
            break