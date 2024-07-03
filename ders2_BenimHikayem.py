
"""
BUGÜN NELER ÖĞRENDİK : 

 Python da birden fazla satır ile çıktı almanın biraz zor bir işlem olduğunu ama 
 bunu daha kolay bir hale getirmek için 3 tırnak kullanabileceğimizi

 bu 3 tırnağın başına f yazmamız durmunda içine istediğimiz değişkenleri de {} 
 kullanarak yazabileceğimizi, ve hatta bir hikaye oluşturabileceğimizi,

 Metametik işlemlerinden bölme işleminin kalanını
 ve sayıların kuvvetini almayı öğrendik ve uygulamalarını yaptık.

"""
print("Merhaba Arkadaşlar Günaydın?\nBu aslında çok satırlı bir metin\nAma Tek satır gibi görünebilir\nBu görüntü sizi yanıltmasın...\n:)")

mtn="""
Bu benim masalim
Bu benim hikayem
yalnız taştan duvar olmaz
bunu yaz yer bi'yere
"""

yas=input("Yasinizi Girin:")

kek=f"""
    
    {yas}
    ||
   [**]
  [****]
 [******]
[********]
"""
print(kek)

ad = input("Adınızı Girin")
sevdiginYemek = input("Sevdiğin Yemek:")
sevdiginRenk = input("Sevdigin Renk : ")
kediminAdı = input("Kedimin adını Gir:")
okulNumaram = input("Okul Numaranı Gir : ")

hikayem=f"""
Merhaba, benim adim {ad},
En sevdigim yemek {sevdiginYemek},
En sevdiğim renk ise {sevdiginRenk},
Bir tane suratsız bir kedim var adi ise {kediminAdı},
Okulda arkadaşlarımı çok seviyorum ve benim okul numaram {okulNumaram}
"""

print(hikayem)

print(127%3)