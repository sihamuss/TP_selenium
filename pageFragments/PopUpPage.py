from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs


class PopUpPage():

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.Btn_viewCart = "//*[contains(text(),'View Cart')]"



    def clickOn_viewCart(self):
         c_Btn_viewCart = self.driver.find_element(By.XPATH, self.Btn_viewCart)
         c_Btn_viewCart.click()