#emcapsule éléments de sélénium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:

    # def __init__(self):
    #     self.driver = None

    def setup_method(self):     #carrespond a before
        options = Options()
        options.add_argument("start-maximized")
        chromedriver_path = 'D:\\chromedriver\\chromedriver.exe'
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.implicitly_wait(15)

    #def teardown_method(self):    #correspond a after
        #if self.driver:
            #self.driver.quit()

    def open_application(self):
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php")