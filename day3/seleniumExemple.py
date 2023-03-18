from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep #chrome kapanmasın dıye
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")#url ler tam url olması onemlı
driver.maximize_window()#tam ekran yapmak ıcın
sleep(2)#10 sn dursun
input = driver.find_element(By.NAME,"q")

input.send_keys("kodlamaio")
searcButton = driver.find_element(By.NAME,"btnK")
print(searcButton)
sleep(2)
searcButton.click()
sleep(2)
firstResut = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a/h3")
sleep(1)
firstResut.click()
sleep(2)
#listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
#print(f"Kodlamaio Sitesinde sunada {len(listOfCourses)} adet kurs var")

#xpathde rsodakı cıft tırkandan sorun cıkarsa tırnakları tek tırnakla değıştir

#send=keysinputa element gondermek icin
while True:
    continue
#html locator 

#fullxpath
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a

#xpaht
#input bulup input ile işlemler yapacak