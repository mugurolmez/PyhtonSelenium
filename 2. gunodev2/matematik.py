class Matematik:
    def __init__(self,sayi1,sayi2):#constructor-yapıcı blok
        self.s1=sayi1#bu blogun ıcındekı degıskenı olusturuyosun fonksıyonlarda sayı1 kullanılabılır
        self.s2=sayi2
        print("matematik başladı(referans olustu)")
        

    def topla(self):
        return self.s1+self.s2
    def cikar(self):
        return self.s1-self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2



matematik =Matematik(14,7)#newleme işlemi gibi
sonuc = matematik.bol()
print("Sonuç: " + str(sonuc))


class Istatistik(Matematik):#inheritance 
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)#super ust sınıfın kendısı
    def varyansHesapla(self):
        return self.s1 * self.s2
    

Istatistik = Istatistik(5,8)
