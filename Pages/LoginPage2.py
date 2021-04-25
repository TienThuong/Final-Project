from selenium.webdriver.support.select import Select

class LoginPage2:
    # Locator element

    # Locator element create
    click_SignIn_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    input_email_id = 'email_create'
    buton_creat_xpath = '//*[@id="SubmitCreate"]'

    # Locator element personal
    input_fistname_id = '//input[@id="customer_firstname"]'

    input_lastname_id = '//input[@id="customer_lastname"]'
    input_pass_id = 'passwd'

    # Locator element address
    # input_add_first_id = 'firstname'
    # input_add_last_id = 'lastname'
    input_address_id = 'address1'
    input_city_id = 'city'
    input_state_id = 'id_state'
    input_zip_id = 'postcode'
    input_country_id = 'id_country'
    input_phone_id = 'phone_mobile'
    input_alias_id = 'alias'
    button_Register_id = 'submitAccount'

    def __init__(self, driver):
        self.driver = driver

    def clickSignIn(self):
        self.driver.find_element_by_xpath(self.click_SignIn_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_id(self.input_email_id).send_keys(email)

    def click_create(self):
        self.driver.find_element_by_xpath(self.buton_creat_xpath).click()

    # Locator element personal
    def set_firsname(self, firstname):
        self.driver.find_element_by_xpath(self.input_fistname_id).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.input_lastname_id).send_keys(lastname)

    def set_pass(self, password):
        self.driver.find_element_by_id(self.input_pass_id).send_keys(password)

    def set_address(self, address):
        self.driver.find_element_by_id(self.input_address_id).send_keys(address)

    def set_city(self, city):
        self.driver.find_element_by_id(self.input_city_id).send_keys(city)

    def set_state(self):
        elt = self.driver.find_element_by_id(self.input_state_id)
        drp = Select(elt)
        drp.select_by_value('3')

    def set_zip(self, zipcode):
        self.driver.find_element_by_id(self.input_zip_id).send_keys(zipcode)

    def set_country(self):
        elt1 = self.driver.find_element_by_id(self.input_country_id)
        drp1 = Select(elt1)
        drp1.select_by_visible_text('United States')

    def set_phone(self, phone):
        self.driver.find_element_by_id(self.input_phone_id).send_keys(phone)

    def set_alias(self, alias):
        self.driver.find_element_by_id(self.input_alias_id).clear()
        self.driver.find_element_by_id(self.input_alias_id).send_keys(alias)

    def click_register(self):
        self.driver.find_element_by_id(self.button_Register_id).click()
