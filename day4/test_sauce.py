from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep #chrome kapanmasın dıye
from selenium.webdriver.common.by import By

class Test_Kodlamaio:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
       
        usernameInput.send_keys("1")
        
        passwordInput.send_keys("2")
        
        loginBtn=driver.find_element(By.NAME,"login-button")
        
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"test Sonucu: {testResult}")
 
    
   

        

testClass = Test_Kodlamaio()
testClass.test_invalid_login()

while True:
    continue