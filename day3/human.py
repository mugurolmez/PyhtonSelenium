class Human:
    #built in
    #init initilazer
    def __init__(self,name):#constructor
        self.name=name
        print("bir human instance'i üretildi")
    
    def __str__(self) -> str:#geriye dönüş tipi str
        return f"Str Fonksiyonundan dönen değer: {self.name}"
    
    
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    
    def walk(self):
        print(f"{self.name}Human İs walking..")
