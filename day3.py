from human import Human
import matematik as math

math.bol(20,2)
#sınıflar
#modules
#paket yonetimi



#instance=> örnek

human1=Human("Enes")
human1.name="Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2=Human("Halit")
#nameye deger vermezsek haliti çağırır
human2.talk("selam")
human2.walk()
print(human2)

Human("Melike").talk("merhaba")