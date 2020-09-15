import time
import unittest

from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

# class to test
class TestingE2E(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.getInputSearch()
        logo = homePage.getLogo().text
        assert "GREENKART" == logo
        product_names = homePage.getProductNames()
        for product_name in product_names:
            print(product_name.text)
        products = homePage.getButtons()
        for product in products:
            product.click()
        homePage.getCartIcon().click()
        homePage.getCheckoutButton()
        time.sleep(3)




