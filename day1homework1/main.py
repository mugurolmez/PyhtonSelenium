sayac=100 # tam sayı tanımlama
km = 1000 #virgüllü sayı tanımlama
ad="ugur" # katar string tanımlama
a=b=c=1     #çoklu atama tum harfler 1 değerini alır 
a,d,f =1,2,"konya" # a 1, d 2 integer olur f "konya " string katar olur
print (id(a)) #a değeşkeninin adresini öğrenme a=b=c=1 tüm değikenlerin adresi aynı olur

#standart veri tipleri
#sayılar (numbers)
#katar(string)
#liste(list)
#tuple
#dictinary

#del var_1 gereksız degısken oldugunda sılınerek belek daha etkin kullanılabilir

#SAYILAR
#int(tam sayılar) 100
#float(kesirli sayılar) 100.232
#complex(karmaşık sayılar) 3.4j

#KATARLAR(strings)
#+ işareti javadaki gibi metin birleştirmeye yarar
#* işareti metin değeri tekrarlamaya yarar

#print(str)          * Tüm katarı yazar
#print(str[0])       * İlk karakteri yazar
#print(str[2:5])     * 3 ile 5. karakter arasını yazar.
#print(str[2:])      * 3. karakterden başlayarak son karaktere kadar yazar.
#print(str * 2)      * 2 kere yazar
#print(str + " yeni string") # Birleştirme işlemi yapar

#LİSTELER(Lists)
#liste içerisine birden fazla farklı tip yerleştirile bilir
#köşeli parantez içinde tanımlanan virgülle birbirinden ayrılan değerler içerir
# list1 = [ 'abcd', 786 , 2.23, 'Çorlu', 70.2 ]
# list2 = [123, 'Merhaba']
# print(list1)          # Tüm listeyi yazar
# print(list1[0])       # İlk öğeyi yazar
# print(list1[1:3])     # 2. öğe ile 3. öğeyi yazar
# print(list1[2:])      # 3. öğeden sonrasını yazar
# print(list2 * 2)  # İki kere yazar
# print(list1 + list2) # İki listeyi birleştirir

#TUPLES
#listeye benzerdir farkı köşeli parantez terine parantezler içinde kullanılır
#ve içerik read-only salt okunurdur değiştirilemez

# tuple1 = ('abcd', 786 , 2.23, 'Çorlu', 70.2)
# tuple2 = (123, 'Merhaba')
# print(tuple1)          # Tüm tuple öğelerini yazar
# print(tuple1[0])       # İlk öğeyi yazar
# print(tuple1[1:3])     # 2. öğe ile 3. öğeyi yazar
# print(tuple1[2:])      # 3. öğeden sonrasını yazar
# print(tuple2 * 2)  # İki kere yazar
# print(tuple1 + tuple2) # İki tupleyi birleştirir

#SÖLÜK(Dictionary)
#0küme parantezleri ({}) ile çevrelenir
#listelerde değerlere ulasmak inin döngüye ve if cloguna ihtiyas vardo ama burda
#daha once verdiğimiz degereulaşmak için anahtarı kullanamız yeterlidir 
#buda en hızlı verı erışimini sağlar

# dict1 = {} #boş bir dictinary
# dict1['one'] = "Anahtar değeri string olarak one - Değer kısmı" 
# dict1[2]     = "Anahtar değeri int olarak 2 - Değer kısmı"
 
# dict2 = {'name': 'Çorlu','code':5901, 'dept': 'Bilgisayar Mühendisliği'}
# #anahtar ve değer verileri ilk atama aşamasında alınıyor.
 
# print(dict1['one'])       # One anahtarının değerini döndürür
# print(dict1[2])           # 2 anahtarının değerini döndürür
# print(dict2)          # Tüm sözlüğü yazar
# print(dict2.keys())   # Tüm anahtarları yazar
# print(dict2.values()) # Tüm değerleri yazar


egitmen = ['Engin Demiroğ', 'Halit Enes Kalayci']
secim=3
if secim==1:
    print("Eğitmeniniz "+egitmen[0])
elif secim==2:
    print("Eğitmeniniz "+egitmen[1])
else:
    print("Geçerli bir seçim yapmadınız")