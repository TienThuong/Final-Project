import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()
import unittest
import time
from Pages.Search1Page import Search1Page


class search1Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        print('Test start')
        print('------------------------------------')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search1(self):
        something = 'Dress'
        search = Search1Page(self.driver)
        search.click_search()
        search.input_something(something)
        time.sleep(3)
        search.clear_search()
        time.sleep(2)

        checkbox = search.check_search()
        self.assertEqual('Search', checkbox, 'This text is not matching')

    def tearDown(self):
        self.driver.quit()
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
