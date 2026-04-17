import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..")) # .. on remontepip

from helpers.BaseTest import BaseTest
from pages.HomePage import HomePage
from pageFragments.HeaderPageFragment import HeaderPageFragment
from pages.productListPage import productListPage
from pages.ProductPage import ProductPage
from pageFragments.PopUpPage import PopUpPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from time import sleep

class Test_FirstTest(BaseTest): # héritage

    @pytest.mark.test_MyFirstTest
    def test_MyFirstTest(self):
        print("My First Test")
        self.open_application()

        home = HomePage(self.driver)
        home.is_page_visible("Your Store")


        header = HeaderPageFragment(self.driver)
        header.select_menu()
        header.select_subMenu()


        productList = productListPage(self.driver)
        productList.check_FilterInStock()
        sleep(3)
        productList.select_img_ProductItem()


        product = ProductPage(self.driver)
        product.click_addToCart()
        sleep(3)

        PopUp = PopUpPage(self.driver)
        PopUp.clickOn_viewCart()
        

        cart = CartPage(self.driver)
        cart.click_checkout()

        Checkout = CheckoutPage(self.driver)
        Checkout.clickOn_checkout()
        Checkout.fill_mandatory_page("siham", "messrar", "messrarsiham300@gmail.com", "0748230897", "54 boulevard pasteur","France, Metropolitane","")
        

       


