class Newletter:

    input_letter_id = 'newsletter-input'
    button_letter_name = 'submitNewsletter'

    def __init__(self, driver):
        self.driver = driver

    def set_letter(self, email):
        self.driver.find_element_by_id(self.input_letter_id).clear()
        self.driver.find_element_by_id(self.input_letter_id).send_keys(email)

    def click_sendletter(self):
        self.driver.find_element_by_name(self.button_letter_name).click()