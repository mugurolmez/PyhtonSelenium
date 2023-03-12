faiz = 1.59
vade = 36
krediAdi="İhtiyaç Kredisi"

#type değişken türünü yazdırma
print(type(faiz))
print(type(vade))
print(type(krediAdi))

#int() vadeyi integera çevir
print(int(vade)+12)
faiz=str(faiz)
print(type(faiz))
#input kullanıcı girdisi alma fonksiyonu
#kullanılıcıdan alınan ınput varsayılan string olarak gelir
#vade=int(input("lütfen giriş yapın")) direk integer olarak değer almak için
# vade=input("lütfen istediğiniz vade sayısını giriniz: ")
print(type(vade))
print(int(vade)+12)
vade= vade + 12

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:          #str dönüştürme
print("seçtiğiniz vade sonucu ortaya çıkan vade: "+str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")
#isim =input("isminizi giriniz")
metin="merhaba {name}".format(name="Samet")
print(metin)

#f-string
metin=f"Hoşgeldiniz {1+1}"
print(metin)

#listeler
#döngüler
#fonksiyonlar
dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)
krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler[0])

#len uzunluk değerini kac elemana sahıp oldugunu gosteri
print(len(krediler))
#print(krediler[3] hata verir


#listenın son elemanına ekleme yapar
krediler.append("Özel Kredi")
print(krediler)
krediler.append("X kredisi")
print(krediler)

#.pop index vermezen son elemanı siler index verirsen verdiğin indexi siler
krediler.pop(0)
print

#değer bazlı çalısır
krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi")
print(krediler)

#diziye birden fazla değer eklemek için kullanılır
krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

#for

#i=10 i<10 
#range 10 dahil değil

for i in range(10):
    print("xx")
    print(i)
print("************")

for i in range(5,10):
    print(i)

print("***********")
for i in range(0,51,10):
    print(i)
print("***************")
#for i in range(0.1,0.5):
#    print(i)

#kredi takma isim krediler kredilerin icini dolas teker teker demek
krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*****************")
for i in range(len(krediler)):
    print(krediler[i])  
print("**************")


#sonsuz döngü
i=0
while i<10:
    print("x")
    #i 1 1 arttır i=i+1 le aynı anlamda i++ pyhtonda kullanılmıyor
    i+=1
print("y")
print("***********************")
#ctrl c progarmı durdurur termınalde


while True:
    print("X")
    break#break döngüyü kırıyor

print("**************")

i=0
while i<len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i]=="Konut Kredisi":
        break

#fonsiyonlar

fiyat=100
indirim = 20
yeniFiyat=fiyat = fiyat - indirim


#definition define fonksiyon tanımlama
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print()

def sayHello(name):
    print(f"merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
calculate()
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")
#void
def calculatePrice(price,discount):
    print(price-discount)

def calculateAndReturn(price,discount):
    return price-discount
print("***************")
fonk1=calculatePrice(100,50)
fonk2=calculateAndReturn(300,100)
print(f"159.satır: {fonk1+100}")
print(f"160.satır: {fonk2+100}")
print("**********************")