from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs


class productListPage:

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.lbl_AvaibilityFilter = "//label[@for='mz-fss-0--1']"
         self.img_ProductItem = '(//div[@class="carousel-item active"]/img[@class="lazy-load"])[3]'




    def check_FilterInStock(self):
         c_lbl_AvaibilityFilter = self.driver.find_element(By.XPATH, self.lbl_AvaibilityFilter)
         c_lbl_AvaibilityFilter.click()

    def select_img_ProductItem(self):
         c_img_ProductItem = self.driver.find_element(By.XPATH, self.img_ProductItem)
         c_img_ProductItem.click()
         