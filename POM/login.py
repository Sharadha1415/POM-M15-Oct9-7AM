import time


'''
STEP1   :   In https://demowebshop.tricentis.com/, we are clicking on login and filling the login data
            execute this file only
'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('link text', 'Log in').click()
# driver.find_element('id', 'Email').send_keys('hari@gmail.com')
# driver.find_element('id', 'Password').send_keys('hari@12345')
#
# ######################################################################################
#
'''
STEP2   :   We defined class(attributes) for the automation script.
            Here only we are creating the object and calling the attributes
            This step execution is happening here only
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# class Login:
#
#     def click_on_login_link(self):
#         driver.find_element('link text', 'Log in').click()
#
#     def enter_login_email(self, email):
#         driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_login_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
# login_obj = Login()
# login_obj.click_on_login_link()
# login_obj.enter_login_email('hari@gmail.com')
# login_obj.enter_login_pwd('hari@12345')
#

# ######################################################################################
#
'''
STEP3   :   We removed the login_obj and calling the attributes and gave it in test_file.
            In this file only Login class and its attributes are present.
            Object creation and calling the attributes is present in test_login.py
            Execution happens in test_login.py 
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# class Login:
#
#     def click_on_login_link(self):
#         driver.find_element('link text', 'Log in').click()
#
#     def enter_login_email(self, email):
#         driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_login_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)

######################################################################################

'''
STEP4   :   We removed initialization of driver and launching of the web-application and gave it in test_login.py 
            Execution in test_login.py
'''

# class Login:
#
#     def click_on_login_link(self):
#         driver.find_element('link text', 'Log in').click()
#
#     def enter_login_email(self, email):
#         driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_login_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
# ## NameError
# ## driver is not present in this file

######################################################################################

'''
STEP5   :   We defined __init__ and we are giving driver as a parameter.
            So, self.driver --> driver = webdriver.Chrome()

            We will replace driver with self.driver

            Execution in test_login.py
'''

# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver            ## self.driver --> driver --> webdriver.Chrome(opts)
#
#     def click_on_login_link(self):
#         self.driver.find_element('link text', 'Log in').click()
#
#     def enter_login_email(self, email):
#         self.driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_login_pwd(self, pwd):
#         self.driver.find_element('id', 'Password').send_keys(pwd)
#

######################################################################################

'''
STEP6
'''

# from object_repository.login_locators import LoginLocators
#
# l_loc = LoginLocators()
#
# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver            ## self.driver --> driver --> webdriver.Chrome(opts)
#
#     def click_on_login_link(self):
#         # self.driver.find_element('link text', 'Log in').click()
#         self.driver.find_element(*l_loc.login_link).click()
#
#     def enter_login_email(self, email):
#         # self.driver.find_element('id', 'Email').send_keys(email)
#         self.driver.find_element(*l_loc.login_email).send_keys(email)
#
#     def enter_login_pwd(self, pwd):
#         # self.driver.find_element('id', 'Password').send_keys(pwd)
#         self.driver.find_element(*l_loc.login_pwd).send_keys(pwd)

# ######################################################################################

'''
STEP6
'''
#
# from object_repository.login_locators import LoginLocators
#
# l_loc = LoginLocators()
#
# class SeleniumWrapper:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_on_ele(self, var_name):
#         self.driver.find_element(*var_name).click()
#
#     def enter_data(self, var_name, data):
#         self.driver.find_element(*var_name).send_keys(data)
#
# class Login:
#
#     def __init__(self, driver):
#         self.driver = driver            ## self.driver --> driver --> webdriver.Chrome(opts)
#         self.wrap_obj = SeleniumWrapper(driver)
#
#     def click_on_login_link(self):
#         # self.driver.find_element(*l_loc.login_link).click()
#         self.wrap_obj.click_on_ele(l_loc.login_link)
#
#     def enter_login_email(self, email):
#         # self.driver.find_element(*l_loc.login_email).send_keys(email)
#         self.wrap_obj.enter_data(l_loc.login_email, email)
#
#     def enter_login_pwd(self, pwd):
#         # self.driver.find_element(*l_loc.login_pwd).send_keys(pwd)
#         self.wrap_obj.enter_data(l_loc.login_pwd, pwd)
#
#


######################################################################################

'''
STEP6
'''

from object_repository.login_locators import LoginLocators
from generic_utilities.selenium_wrapper import SeleniumWrapper

l_loc = LoginLocators()

class Login:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> driver --> webdriver.Chrome(opts)
        self.wrap_obj = SeleniumWrapper(driver)

    def click_on_login_link(self):
        self.wrap_obj.click_on_ele(l_loc.login_link)

    def enter_login_email(self, email):
        self.wrap_obj.enter_data(l_loc.login_email, email)

    def enter_login_pwd(self, pwd):
        self.wrap_obj.enter_data(l_loc.login_pwd, pwd)





















