print("kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
#string metinsel ifade
baslik="İntiyaç Kredisi"
print(baslik)

vade = 36
ekVade= 6
vade2= "36"
#float,decimal,double ondalıklı sayı değişkenleri
aylikOdeme = 200.50


#bool, boolean => True veya False
yukselistemi= True

#matematisel operatörler
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36+6)

#-
print(5-5)
print(vade-5)
print(vade-ekVade)




# *
print(5*5)
print(vade*2)
print(vade*ekVade)
print(10*10)

#/
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

#% => mod operator
print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


#mantıksal operatörler
print(1==1)#eşit mi 
print(1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1 < 2)
print(3<1)
print(1<1)
print(1<=1)



print(1 !=1)
print(1!= 2)

#or and

#or => veya
print(1>2 or  5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)
#okumaya soldan başlıyor ılk operator ıslemı yapıldıkdan
#sonra diger degerke karsılastırıyor
print(1<2 and 5>2 and 3>2)



#karar yapıları
#if else

sayi1 = 15
sayi2 = 15
#sayi1 sayi2 den büyükse ekrana sayi 1 daha  büyük yazdır
#condition
if sayi1<sayi2:
    print("sayi 1 sayi 2 den büyüktür")
elif sayi1==sayi2:
    print("iki sayi eşittir")
#eğer if bloduna girmezse 
else:
    print("sayi1 sayi 2den küçüktür")

print("************************")


if sayi1<=sayi2:
    print("sayi 1 sayi 2 den küçüktür")
if sayi1==sayi2:
    print("iki sayi eşittir")
else:
    print("Sayi1 sayi2den büyükyür")

print("burası if blogunun dışıdır")
