
from selenium.webdriver.common.by import By
URL = "https://www.saucedemo.com/"
labsBackPackURL="https://www.saucedemo.com/inventory-item.html?id=4"
inventoryURL="https://www.saucedemo.com/inventory.html"
standardUser="standard_user"
lockedUsername="locked_out_user"
password = "password"
userName = "user-name"
cartItem = "cart_item"
loginButton = "login-button"
errorButton = "error-button"
inventoryItem = "inventory_item"
inventoryItemName="inventory_item_name"
shopingCartLinkLocator =(By.CLASS_NAME,"shopping_cart_link")
shopingCartLinkValue="shopping_cart_link"
inventoryContainerLocator = (By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]")
sauceLabsBackpacklocator= (By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]")
sauceLabsBackpackXpath="/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div"
backToProtuctLocator = (By.CSS_SELECTOR, "*[data-test=\"back-to-products\"]")
backtoProductcsselector="*[data-test=\"back-to-products\"]"
productsTittleLocator=(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")
productsTitleXpath= "/html/body/div/div/div/div[1]/div[2]/span"
checkoutLocator =(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
checkoutSelector ="*[data-test=\"checkout\"]"



secretSauce = "secret_sauce"
cartList = "add-to-cart-sauce-labs-backpack","add-to-cart-sauce-labs-bike-light","add-to-cart-sauce-labs-bolt-t-shirt","add-to-cart-sauce-labs-fleece-jacket","add-to-cart-sauce-labs-onesie","add-to-cart-test.allthethings()-t-shirt-(red)"

errorMessageLocator = By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"

errorMessageValue ="/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"
nullNameAndPasswoerdErrorMessage = "Epic sadface: Username is required"
nullPasswordErrorMessage ="Epic sadface: Password is required"
lockedUserErrorMessage = "Epic sadface: Sorry, this user has been locked out."


