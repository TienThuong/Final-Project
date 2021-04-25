class LoginPage:
    # Locator of login element
    link_signin_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    email_input_id = 'email_create'
    button_login_id = 'SubmitCreate'

    def __init__(self, driver):
        self.driver = driver

    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.link_signin_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_id(self.email_input_id).clear()
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    def click_login(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def check_message(self):
        return self.driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li').text