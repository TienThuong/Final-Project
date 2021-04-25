import unittest
import time
from selenium import webdriver
import chromedriver_autoinstaller
from Pages.Newletter import Newletter
chromedriver_autoinstaller.install()

class Send_Letter(unittest.TestCase):
    email = 'buiyenoanh901@gmail.com'

    def setUp(cls):
        print("Initiating Chrome driver")
        cls.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://automationpractice.com/")
        cls.driver.maximize_window()
    def test_letter(self):
        lt = Newletter(self.driver)
        lt.set_letter(self.email)
        lt.click_sendletter()
        time.sleep(5)

        if self.driver.find_element_by_xpath('//*[@id="columns"]/p'):
            self.assertTrue(True)
        else:
            self.assertFalse(False)

    def tearDown(cls):
        cls.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()