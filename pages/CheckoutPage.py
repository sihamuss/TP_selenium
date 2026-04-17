from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs


class CheckoutPage:

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.btn_select_guest ="//label[contains(text(),'Guest Checkout')]"
         self.fill_field_firstName = "//input[@name='firstname']"
         self.fill_field_lastName = "//input[@name='lastname']"
         self.fill_field_email = "//input[@name='email']"
         self.fill_field_number = "//input[@name='telephone']"
         self.fill_field_address_1 = "//input[@name='address_1']"
         self.fill_field_city = "//input[@name='city']"
         self.fill_field_postCode = "//input[@name='postcode']"
         self.fill_field_country = "//select[@name='country_id']"
         self.fill_field_state = "//select[@name='zone_id']"



    def clickOn_checkout(self):
          c_Btn_guest_checkout = self.driver.find_element(By.XPATH, self.btn_select_guest)
          c_Btn_guest_checkout.click()

    def fill_mandatory_page(self, name : str, prenom: str, email: str, number: str, address: str, city : str, postCode: str, Country: str, state: str):
         c_firstName_input = self.driver.find_element(By.XPATH, self.fill_field_firstName)
         c_firstName_input.send_keys(name)
         c_lastName_input = self.driver.find_element(By.XPATH, self.fill_field_lastName)
         c_lastName_input.send_keys(prenom)
         c_email_input = self.driver.find_element(By.XPATH, self.fill_field_email)
         c_email_input.send_keys(email)
         c_number_input = self.driver.find_element(By.XPATH, self.fill_field_number)
         c_number_input.send_keys(number)
         c_address_input = self.driver.find_element(By.XPATH, self.fill_field_address_1)
         c_address_input.send_keys(address)
         c_city_input = self.driver.find_element(By.XPATH, self.fill_field_city)
         c_city_input.send_keys(city)
         c_postCode_input = self.driver.find_element(By.XPATH, self.fill_field_postCode)
         c_postCode_input.send_keys(postCode)
         select_country = self.driver.find_element(By.XPATH, self.fill_field_country)
         select = select(select_country)
         select.select_by_visible_text(Country)
         select_state = self.driver.find_element(By.XPATH, self.fill_field_state)
         select = select(select_state)
         select.select_by_visible_text(state)


         




