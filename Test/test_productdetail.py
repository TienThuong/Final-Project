import time
import unittest
from parameterized import parameterized
import chromedriver_autoinstaller
from selenium import webdriver

from Pages.ProductDetail import ProductDetail

chromedriver_autoinstaller.install()


class test_prodetail(unittest.TestCase):
    def setUp(self):
        print('Test start')
        print('-----------------------')

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    # check viewlarge when clicking
    def test_viewlarge(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        check_viewlarge = ProductDetail(self.driver)
        check_viewlarge.click_proInto_list()
        time.sleep(2)
        check_viewlarge.click_image_detail()
        time.sleep(2)
        normal_image = check_viewlarge.get_size_normal_image()
        big_image = check_viewlarge.get_size_big_image()
        size_normal_image = normal_image.get('height')
        siz_big_image = big_image.get('height')

        if size_normal_image > siz_big_image:
            print('Big image does not displayed')
        elif size_normal_image == siz_big_image:
            print('Big image is not zoom in')
        else:
            print('Big image is displaying')

        location_image = check_viewlarge.get_location_bigimage()
        get_location_image = location_image.get('y')
        location_name = check_viewlarge.get_location_name()
        get_location_name = location_name.get('y')
        if get_location_image > get_location_name:
            print('This name is not show below the image')
        elif get_location_image == get_location_name:
            print('This name is not show belong the image')
        else:
            print('This name is show below the image')
        time.sleep(5)

    # check viewlarge when clicking button view large
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_click_button(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        check_click_button = ProductDetail(self.driver)
        check_click_button.click_proInto_list()
        time.sleep(5)
        check_click_button.click_image_detail()
        time.sleep(2)
        check_click_button.click_button_close()
        time.sleep(1)
        check_click_button.click_button_viewlarge()
        time.sleep(2)
        normal_image = check_click_button.get_size_normal_image()
        big_image = check_click_button.get_size_big_image()
        size_normal_image = normal_image.get('height')
        siz_big_image = big_image.get('height')

        if size_normal_image > siz_big_image:
            print('Big image does not displayed')
        elif size_normal_image == siz_big_image:
            print('Big image is not zoom in')
        else:
            print('Big image is displaying')

        location_image = check_click_button.get_location_bigimage()
        get_location_image = location_image.get('y')
        location_name = check_click_button.get_location_name()
        get_location_name = location_name.get('y')
        if get_location_image > get_location_name:
            print('This name is not show below the image')
        elif get_location_image == get_location_name:
            print('This name is not show belong the image')
        else:
            print('This name is show below the image')
        time.sleep(5)

    # add to cart with quantity = 0
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_quantityzero(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        input_key = 0
        check_quantityzero = ProductDetail(self.driver)
        check_quantityzero.click_proInto_list()
        time.sleep(2)
        check_quantityzero.click_image_detail()
        time.sleep(1)
        check_quantityzero.click_button_close()
        check_quantityzero.clear_input()
        check_quantityzero.input_quantity(input_key)
        time.sleep(1)
        check_quantityzero.click_addtoCart()
        title = check_quantityzero.check_alert()
        self.assertEqual('Null quantity.', title, 'This alert is not matching')
        time.sleep(5)

    # add to cart with quantity >0
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_quantity(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        input_key = 0
        input_keys = 1
        check_quantity = ProductDetail(self.driver)
        check_quantity.click_proInto_list()
        time.sleep(2)
        check_quantity.click_image_detail()
        time.sleep(1)
        check_quantity.click_button_close()
        check_quantity.clear_input()
        check_quantity.input_quantity(input_key)
        time.sleep(1)
        check_quantity.click_addtoCart()
        time.sleep(1)
        check_quantity.close_button_alert()
        check_quantity.clear_input()
        check_quantity.input_quantity(input_keys)
        time.sleep(3)
        check_quantity.click_addtoCart()
        time.sleep(3)
        title = check_quantity.get_alert_success()
        self.assertEqual('Product successfully added to your shopping cart',
                         title, 'The title ís not matching')
        check_quantity.close_popup()
        get_name_detail = check_quantity.get_name_detail()
        get_quantity_detail = check_quantity.get_quantity_detail()
        time.sleep(2)
        check_quantity.click_button_cart()
        get_name_cart = check_quantity.get_name_cart()
        get_quantity_cart = check_quantity.get_quantity_cart()
        if get_name_detail == get_name_cart:
            if get_quantity_detail == get_quantity_cart:
                print('This product is successfully added to the cart')
        time.sleep(2)

    # test share to twitter
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_sharetwitter(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        share_twitter = ProductDetail(self.driver)
        share_twitter.click_proInto_list()
        time.sleep(3)
        share_twitter.click_button_twitter()
        self.driver.switch_to.window(self.driver.window_handles[1])

    # test write comment
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_write_comment(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        user = 'nam99@gmail.com'
        pw = '@@q7vLZDt2PdmuG'
        title = 'How nice this product'
        content = 'This product is so nice and I love it so much'
        write_comment = ProductDetail(self.driver)
        write_comment.click_signIn()
        write_comment.input_account(user, pw)
        time.sleep(1)
        write_comment.click_button_sign()
        write_comment.click_backHome()
        time.sleep(2)
        write_comment.click_proInto_list()
        time.sleep(2)
        write_comment.click_writecmt()
        write_comment.write_cmt(title, content)
        time.sleep(2)
        write_comment.click_sendcmt()
        time.sleep(2)
        title = write_comment.get_title_success()
        self.assertEqual('Your comment has been added and will be available once approved by a moderator',
                         title, 'This notice is not matching')
        write_comment.close_notice_success()
        time.sleep(10)

    # test send to friend
    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_send_toFriend(self,browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"F:/Driver/geckodriver.exe")
            time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        user = 'Nguyen Van Nam'
        email = 'Nguyenvannam@gmail.com'
        send_toFriend = ProductDetail(self.driver)
        send_toFriend.click_proInto_list()
        time.sleep(2)
        send_toFriend.click_send()
        send_toFriend.input_content(user, email)
        time.sleep(1)
        send_toFriend.click_send_email()
        time.sleep(1)
        title = send_toFriend.get_send_email()
        self.assertEqual('Your e-mail has been sent successfully',
                         title, 'This notice is not matching')
        time.sleep(3)
        send_toFriend.click_close_send_email()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        print('-----------------------')
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
