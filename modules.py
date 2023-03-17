#allias takma ad as ile kullanılıyor
from matematik import topla as toplamaIslemi
from day2 import sayHello
from human import Human
import random #ragele sayı ureten modul
from selenium import webdriver
#package
print(toplamaIslemi(10,20))

#0 ve 100 dahil rasgele sayı uret
print(random.randint(0,100))

human1=Human("Mirza")
human1.talk("Merhaba")

cromeDriver = webdriver.Chrome()

#packages