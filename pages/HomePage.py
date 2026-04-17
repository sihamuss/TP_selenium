from selenium.webdriver.remote.webdriver import WebDriver
# https://googlechromelabs.github.io/chrome-for-testing/ site pour télécharger les navigateurs


class HomePage:

    def __init__(self, driver: WebDriver):
         self.driver = driver
         self.__website_title = "Your Store"

    def is_page_visible(self, wishedValue: str):
        current_website_title = self.driver.title
        print(f"My current title is : {current_website_title}") # à remplacer par un logger
        assert current_website_title == wishedValue


