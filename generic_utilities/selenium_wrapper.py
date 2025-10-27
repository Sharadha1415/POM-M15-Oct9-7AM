class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_on_ele(self, var_name):
        self.driver.find_element(*var_name).click()

    def enter_data(self, var_name, data):
        self.driver.find_element(*var_name).send_keys(data)
