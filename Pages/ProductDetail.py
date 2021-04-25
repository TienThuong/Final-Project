import random
import time


class ProductDetail:
    # Locator

    # check viewlarge when clicking image
    lst_product = '//*[@id="homefeatured"]/li'
    normal_image = '//*[@id="bigpic"]'
    big_image = '//div[@class="fancybox-wrap fancybox-desktop fancybox-type-image fancybox-opened"]'
    title_xpath = '//span[@class = "child"]'

    # check viewlarge when clicking button view large
    button_close = '//a[@class="fancybox-item fancybox-close"]'

    button_viewlarge = '//span[@class="span_link no-print"]'

    # add to cart with quantity =0

    quantity_xpath = '//input[@id="quantity_wanted"]'

    buton_addtocart = '//*[@id="add_to_cart"]/button/span'

    alert_quantity = '//p[@class="fancybox-error"]'

    # add to cart with quantity >0

    close_alert_xpath = '//a[@class="fancybox-item fancybox-close"]'
    alert_success_xpath = '//*[@id="layer_cart"]/div[1]/div[1]/h2'
    button_close_popup = '//*[@id="layer_cart"]/div[1]/div[1]/span'
    button_cart_xpath = '//*[@id="header"]/div[3]/div/div/div[3]/div/a'

    get_name_detail_xpath = '//div[@class="pb-center-column col-xs-12 col-sm-4"]//h1'
    get_quantity_detail_xpath = '//p//input[@id="quantity_wanted"]'
    get_name_cart_xpath = '//tr//td//p[@class="product-name"]/a'
    get_quantity_cart_xpath = '//td[@class="cart_quantity text-center"]/input[1]'

    # test social network

    twitter = '//*[@id="center_column"]/div/div/div[3]/p[7]/button[1]'
    user_name = '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    pw = '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    login = '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]'
    mail = '//*[@id="send_friend_button"]'

    # test write comment
    click_sign = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    user_xpath = '//*[@id="email"]'
    pw_xpath = '//*[@id="passwd"]'
    button_signIn = '//*[@id="SubmitLogin"]'
    button_backHome = '//*[@id="center_column"]/ul/li/a'
    click_write_cmt = '//a[@class="open-comment-form"]'
    input_title = '//*[@id="comment_title"]'
    input_comment = '//*[@id="content"]'
    button_send_cmt = '//*[@id="submitNewMessage"]'
    check_title = '//*[@id="product"]/div[2]/div/div/div/p[1]'
    close_notice = '//*[@id="product"]/div[2]/div/div/div/p[2]/button'

    # test send to friend
    send_to_friend = '//*[@id="send_friend_button"]'
    name_xpath = '//*[@id="friend_name"]'
    email_xpath = '//*[@id="friend_email"]'
    button_send_mail = '//*[@id="sendEmail"]'
    notice_send_mail = '//*[@id="product"]/div[2]/div/div/div/p[1]'
    close_send_email = '//*[@id="product"]/div[2]/div/div/div/p[2]/input'

    def __init__(self, driver):
        self.driver = driver

    # check viewlarg when clicking image
    def click_proInto_list(self):
        lst_pro = self.driver.find_elements_by_xpath(self.lst_product)
        random.choice(lst_pro).click()

    def click_image_detail(self):
        self.driver.find_element_by_xpath(self.normal_image).click()

    def get_size_normal_image(self):
        size_image = self.driver.find_element_by_xpath(self.normal_image).size
        return size_image

    def get_size_big_image(self):
        size_image = self.driver.find_element_by_xpath(self.big_image).size
        return size_image

    def get_location_bigimage(self):
        image_location = self.driver.find_element_by_xpath(self.big_image)
        return image_location.location

    def get_location_name(self):
        title_location = self.driver.find_element_by_xpath(self.title_xpath).location
        return title_location

    # check viewlarge when clicking button view large

    def click_button_close(self):
        self.driver.find_element_by_xpath(self.button_close).click()

    def click_button_viewlarge(self):
        self.driver.find_element_by_xpath(self.button_viewlarge).click()

    # add to cart with quantity = 0

    def clear_input(self):
        self.driver.find_element_by_xpath(self.quantity_xpath).clear()

    def input_quantity(self, input_key):
        self.driver.find_element_by_xpath(self.quantity_xpath).send_keys(input_key)

    def click_addtoCart(self):
        self.driver.find_element_by_xpath(self.buton_addtocart).click()

    def check_alert(self):
        alert_quantityrezo = self.driver.find_element_by_xpath(self.alert_quantity).text
        return alert_quantityrezo

    # add to cart with quantity >0
    def close_button_alert(self):
        self.driver.find_element_by_xpath(self.close_alert_xpath).click()

    def get_alert_success(self):
        return self.driver.find_element_by_xpath(self.alert_success_xpath).text

    def close_popup(self):
        self.driver.find_element_by_xpath(self.button_close_popup).click()

    def click_button_cart(self):
        self.driver.find_element_by_xpath(self.button_cart_xpath).click()

    def get_name_detail(self):
        return self.driver.find_element_by_xpath(self.get_name_detail_xpath).text

    def get_quantity_detail(self):
        quantity_detail = self.driver.find_element_by_xpath(self.get_quantity_detail_xpath).get_attribute('value')
        return quantity_detail

    def get_name_cart(self):
        get_name = self.driver.find_element_by_xpath(self.get_name_cart_xpath).text
        return get_name

    def get_quantity_cart(self):
        return self.driver.find_element_by_xpath(self.get_quantity_cart_xpath).get_attribute('value')

    # test share to twitter
    def click_button_twitter(self):
        self.driver.find_element_by_xpath(self.twitter).click()

    # test write comment
    def click_signIn(self):
        self.driver.find_element_by_xpath(self.click_sign).click()

    def input_account(self, username, pw):
        self.driver.find_element_by_xpath(self.user_xpath).send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.pw_xpath).send_keys(pw)

    def click_button_sign(self):
        self.driver.find_element_by_xpath(self.button_signIn).click()

    def click_backHome(self):
        self.driver.find_element_by_xpath(self.button_backHome).click()

    def click_writecmt(self):
        self.driver.find_element_by_xpath(self.click_write_cmt).click()

    def write_cmt(self, title, content):
        self.driver.find_element_by_xpath(self.input_title).send_keys(title)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.input_comment).send_keys(content)

    def click_sendcmt(self):
        self.driver.find_element_by_xpath(self.button_send_cmt).click()

    def get_title_success(self):
        return self.driver.find_element_by_xpath(self.check_title).text

    def close_notice_success(self):
        self.driver.find_element_by_xpath(self.close_notice).click()

    # test send friend
    def click_send(self):
        self.driver.find_element_by_xpath(self.send_to_friend).click()

    def input_content(self, name, email):
        self.driver.find_element_by_xpath(self.name_xpath).send_keys(name)
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def click_send_email(self):
        self.driver.find_element_by_xpath(self.button_send_mail).click()

    def get_send_email(self):
        return self.driver.find_element_by_xpath(self.notice_send_mail).text

    def click_close_send_email(self):
        self.driver.find_element_by_xpath(self.close_send_email).click()
