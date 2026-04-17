from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs


class ProductPage:

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.Btn_addCart = '(//button[contains(text(),"Add to Cart")])[2]'
         


    def click_addToCart(self):
         c_Btn_addCart = self.driver.find_element(By.XPATH, self.Btn_addCart)
         c_Btn_addCart.click()

  
    
         