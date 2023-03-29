
import inspect
from selenium.webdriver.common.by import By

def test_xButton(self):
    self.loginButtonClick() 
    self.xButtonClick()
    
    # Ekran görüntüsü adı, xButtonClick fonksiyonunun adını alarak oluşturuluyor
    functionName = inspect.getframeinfo(inspect.currentframe().f_back).function
    screenshotName = f"{self.folderPath}/{functionName}.png"
    
    # Ekran görüntüsü alıyoruz
    self.driver.save_screenshot(screenshotName)
    
    # Test sonucunu assert ifadesiyle kontrol ediyoruz

    
    # Fonksiyon adını ve ekran görüntüsü adını ekrana yazdırıyoruz
    print(f"Test adı: {functionName}")
    print(f"Ekran görüntüsü adı: {screenshotName}")