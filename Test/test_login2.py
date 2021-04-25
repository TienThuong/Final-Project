import time
import unittest
import chromedriver_autoinstaller
from selenium import webdriver
chromedriver_autoinstaller.install()
from Pages.LoginPage2 import LoginPage2

class Test_login2(unittest.TestCase):

    def setUp(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()

    def test_login2(self):
        email = "buitienthuonggggg@gmail.com"
        firstname = 'oanh'
        lastname = 'ngoc yen'
        password = 'oanh123'
        address = 'Hai Duong'
        city = 'Ha Noi'
        zipcode = 10000
        phone = '0388826899'
        alias = 'Nothing'
        login = LoginPage2(self.driver)
        login.clickSignIn()
        time.sleep(2)
        login.set_email(email)
        time.sleep(2)
        login.click_create()
        time.sleep(3)
        login.set_firsname(firstname)
        time.sleep(3)
        login.set_lastname(lastname)
        time.sleep(3)
        login.set_pass(password)
        time.sleep(3)
        login.set_address(address)
        time.sleep(3)
        login.set_city(city)
        time.sleep(3)
        login.set_state()
        time.sleep(3)
        login.set_zip(zipcode)
        time.sleep(3)
        login.set_phone(phone)
        time.sleep(3)
        login.set_alias(alias)
        time.sleep(2)
        login.click_register()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual('My account - My Store', title, 'This title is matching')

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()
