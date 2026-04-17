from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs


class CartPage:

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_checkout = '//a[contains(text(),"Checkout")]'




    def click_checkout(self):
         c_Btn_checkout = self.driver.find_element(By.XPATH, self.btn_checkout)
         c_Btn_checkout.click()
