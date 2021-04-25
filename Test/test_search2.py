import time
import unittest
import pytest
from selenium import webdriver
from parameterized import  parameterized
from Pages.Search2Page import ProductDetailPage
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


class search2Page(unittest.TestCase):

    def setUp(self):

        print('Test start')
        print('-------------------------')

    # Kiểm tra danh sách gợi ý
    # @unittest.skip
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_search2(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        search = ProductDetailPage(self.driver)
        search.click_box_search()
        search.send_key_to_search(input)
        time.sleep(5)
        list = search.get_list_suggest_keywords()
        for suggest_keyword in list:
            try:
                self.assertIn('Dress', suggest_keyword, 'This word is not in list')
                print('The suggest keyword is matching')
            except:
                print('The suggest keyword is not matching')

    # Kiểm tra text danh sách gợi ý với title
    # @unittest.skip
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_checkvalue_suggest(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        input = 'Dress'
        check_name = ProductDetailPage(self.driver)
        check_name.click_box_search()
        time.sleep(2)
        check_name.send_key_to_search(input)
        time.sleep(3)
        lst_suggest_elt = check_name.check_value_suggest()
        total = len(lst_suggest_elt)
        lst_suggest_elt[0].click()

        for index in range(total):
            check_name.send_key_to_search(input)
            time.sleep(3)
            lst_pro = check_name.get_lst_product()
            elt = lst_pro[index]
            elt_txt = elt.text
            time.sleep(2)
            elt.click()
            title = check_name.get_title()
            if title in elt_txt:
                print('This title is matching')

    # Kiểm tra số lượng sản phẩm khi search
    # @unittest.skip
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_search_quantity(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        input = 'Dress'
        search_quantity = ProductDetailPage(self.driver)
        search_quantity.click_box_search()
        search_quantity.send_key_to_search(input)
        time.sleep(2)
        search_quantity.click_button_search()
        lst_quantity = search_quantity.check_quantity_list()
        title_quantity = search_quantity.check_title_search()

        if lst_quantity == title_quantity:
            print('Thông tin số lượng được hiển thị đúng với số lượng sản phẩm hiển thị')
        else:
            print('This does not matching')

    # Kiểm tra giá sản phẩm khi tìm kiếm
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_check_price(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        input_key = 'Dress'

        # home_page = HomePage(self.driver)
        product_detail_page = ProductDetailPage(self.driver)

        product_detail_page.send_key_to_search(input_key)
        time.sleep(3)
        list_suggest_product_elt = product_detail_page.get_list_suggest_product_elt()  # list suggest in HomePage
        total = len(list_suggest_product_elt)
        time.sleep(2)
        list_suggest_product_elt[0].click()
        if self.driver.find_element_by_id('our_price_display').is_displayed():
            print('The price product is display when searching')
        else:
            print('No price - product is Display')
        for index in range(1, total):
            product_detail_page.send_key_to_search(input_key)
            time.sleep(5)
            lst_product = product_detail_page.get_lst_product()  # list suggest in ProductPage
            elt = lst_product[index]
            elt.click()

            time.sleep(2)
            if self.driver.find_element_by_id('our_price_display').is_displayed():
                print('The price product is displayed')
            else:
                print('No price - product is Display')

    # Kiểm tra kết quả tìm kiếm sau khi nhập sai tên sản phẩm
    # @unittest.skip
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_wrong_keyword(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        input_key = 'dresSSss'
        check_wrong_keyword = ProductDetailPage(self.driver)
        check_wrong_keyword.click_box_search()
        check_wrong_keyword.send_key_to_search(input_key)
        check_wrong_keyword.click_button_search()
        wrong_title = check_wrong_keyword.get_wrong_title()

        self.assertEqual(f'No results were found for your search "{input_key}"', wrong_title,
                         'This notice does not matching')

    def tearDown(self):
        self.driver.quit()
        print('-------------------------')
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
