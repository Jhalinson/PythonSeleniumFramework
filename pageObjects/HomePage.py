import this

from selenium.webdriver.common.by import By

from pageObjects.CartPage import Cart

# class home page simulated a page
class HomePage:
    input_search = (By.XPATH, "//input[@type='search']")
    logo = (By.XPATH, '//div[@class="brand greenLogo"]')
    product_names = (By.XPATH, '//div[@class="product"]//h4')
    buttons = (By.XPATH, '//div[@class="product"]/div/button')
    cart_icon = (By.XPATH, '//a/img[@src="https://res.cloudinary.com/sivadass/image/upload/v1493548928/icons/bag.png"]')
    checkout_button = (By.XPATH, "//div/button[@type='button' and @class= ' ' and text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def getInputSearch(self):
        return self.driver.find_element(*HomePage.input_search).send_keys("ber")

    def getLogo(self):
        return self.driver.find_element(*HomePage.logo)

    def getProductNames(self):
        return self.driver.find_elements(*HomePage.product_names)

    def getButtons(self):
        return self.driver.find_elements(*HomePage.buttons)

    def getCartIcon(self):
        return self.driver.find_element(*HomePage.cart_icon)

    def getCheckoutButton(self):
        self.driver.find_element(*HomePage.checkout_button).click()
        cart = Cart(self.driver)
        return cart