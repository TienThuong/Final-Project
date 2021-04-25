import time
import unittest
from parameterized import parameterized
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from Pages.LoginPage import LoginPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        print("Test is started")
        print("-----------------------------------------")

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_login_success(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        email = 'abc123'
        login = LoginPage(self.driver)
        login.clickSignIn()
        login.set_email(email)
        login.click_login()
        time.sleep(3)

        message = login.check_message()
        self.assertEqual('Invalid email address.', message, 'Email is True')

    def tearDown(self):
        self.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()
