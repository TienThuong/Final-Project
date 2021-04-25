class ProductDetailPage:
    textbox_search_xpath = '//*[@id="search_query_top"]'
    list_suggest_xpath = '//*[@id="index"]/div[2]/ul/li'
    title_xpath = '//*[@id="center_column"]/div/div/div[3]/h1'
    button_search_xpath = '//*[@id="searchbox"]/button'
    list_search_xpath = '//*[@id="center_column"]/ul/li'
    title_result_class_name = 'heading-counter'

    # wrong tittle
    tittle_wrong_xpath = '//*[@id="center_column"]/p'

    # ProductPage
    list_product_xpath = '//*[@id="product"]/div[2]/ul/li'

    def __init__(self, driver):
        self.driver = driver

    def click_box_search(self):
        self.driver.find_element_by_xpath(self.textbox_search_xpath).click()

    def send_key_to_search(self, input_key):
        elt = self.driver.find_element_by_xpath(self.textbox_search_xpath)
        elt.clear()
        elt.send_keys(input_key)

    def click_button_search(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    # Kiểm tra danh sách gợi ý
    def get_list_suggest_keywords(self):
        lst_suggest_keywords = self.driver.find_elements_by_xpath(self.list_suggest_xpath)
        lst_text = []
        for suggest_keyword in lst_suggest_keywords:
            suggest_keyword_text = suggest_keyword.text
            lst_text.append(suggest_keyword_text)
        return lst_text

    # Kiểm tra text danh sách gợi ý với title
    def check_value_suggest(self):
        lst_suggest = self.driver.find_elements_by_xpath(self.list_suggest_xpath)
        return lst_suggest

    def get_title(self):
        return self.driver.find_element_by_xpath(self.title_xpath).text

    # Kiểm tra hiển thị của số lượng sản phẩm khi search
    def check_quantity_list(self):
        lst_search = self.driver.find_elements_by_xpath(self.list_search_xpath)
        new_lst = []
        for lst in lst_search:
            lst_text = lst.text
            new_lst.append(lst_text)
        return len(new_lst)

    def check_title_search(self):
        title = self.driver.find_element_by_class_name(self.title_result_class_name).text
        lst_title = title.split()
        new_lst = []
        for i in lst_title:
            new_lst.append(i)
        return int(new_lst[0])

    # Kiểm tra giá sản phẩm khi tìm kiếm
    def get_list_suggest_product_elt(self):
        lst = self.driver.find_elements_by_xpath(self.list_suggest_xpath)
        # new_lst = []
        # for i in lst:
        #     new_lst.append(i)
        # return new_lst
        return lst

    # get list suggest in ProductPage
    def get_lst_product(self):
        elts = self.driver.find_elements_by_xpath(self.list_product_xpath)
        return elts

    # Kiểm tra khi nhập sai keyword

    def get_wrong_title(self):
        return self.driver.find_element_by_xpath(self.tittle_wrong_xpath).text
