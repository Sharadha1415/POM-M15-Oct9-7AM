import time

'''
STEP1   :   In https://demowebshop.tricentis.com/, we are clicking on register and filling the register data
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
# driver.find_element('link text', 'Register').click()
# driver.find_element('id', 'gender-male').click()
# driver.find_element('id', 'FirstName').send_keys('Harish')
# driver.find_element('id', 'LastName').send_keys('Chikkammanavar')
# driver.find_element('id', 'Email').send_keys('hari@gmail.com')
# driver.find_element('id', 'Password').send_keys('hari@12345')
# driver.find_element('id', 'ConfirmPassword').send_keys('hari@12345')


# ########################################################################################
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
# class Register:
#
#     def click_on_reg_link(self):
#         driver.find_element('link text', 'Register').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email):
#         driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_reg_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(pwd)
#
# reg_obj = Register()
# reg_obj.click_on_reg_link()
# reg_obj.click_on_gender_btn()
# reg_obj.enter_firstname('Harish')
# reg_obj.enter_lastname('Chikkammanavar')
# reg_obj.enter_reg_email('hari@gmail.com')
# reg_obj.enter_reg_pwd('hari@12345')
# reg_obj.enter_confirm_pwd('hari@12345')

########################################################################################

'''
STEP3   :   We removed the reg_obj and calling the attributes and gave it in test_file.
            In this file only Register class and its attributes are present.
            Object creation and calling the attributes is present in test_reg.py
            Execution happens in test_reg.py 
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
# class Register:
#
#     def click_on_reg_link(self):
#         driver.find_element('link text', 'Register').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email):
#         driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_reg_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(pwd)

########################################################################################

'''
STEP4   :   We removed initialization of driver and launching of the web-app and gave it in test_file
'''

# class Register:
#
#     def click_on_reg_link(self):
#         driver.find_element('link text', 'Register').click()
#
#     def click_on_gender_btn(self):
#         driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email):
#         driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_reg_pwd(self, pwd):
#         driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, pwd):
#         driver.find_element('id', 'ConfirmPassword').send_keys(pwd)

########################################################################################

'''
STEP5   :   We defined __init__ and we are giving driver as a parameter.
            So, self.driver --> driver = webdriver.Chrome()
            
            We will replace driver with self.driver
            
            Execution in test_reg.py
'''

# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver --> webdriver.Chrome(opts)
#
#     def click_on_reg_link(self):
#         self.driver.find_element('link text', 'Register').click()
#
#     def click_on_gender_btn(self):
#         self.driver.find_element('id', 'gender-male').click()
#
#     def enter_firstname(self, fname):
#         self.driver.find_element('id', 'FirstName').send_keys(fname)
#
#     def enter_lastname(self, lname):
#         self.driver.find_element('id', 'LastName').send_keys(lname)
#
#     def enter_reg_email(self, email):
#         self.driver.find_element('id', 'Email').send_keys(email)
#
#     def enter_reg_pwd(self, pwd):
#         self.driver.find_element('id', 'Password').send_keys(pwd)
#
#     def enter_confirm_pwd(self, pwd):
#         self.driver.find_element('id', 'ConfirmPassword').send_keys(pwd)


########################################################################################

'''
STEP6
'''

# from object_repository.reg_locators import RegisterLocators
#
# r_loc = RegisterLocators()
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver  ## self.driver --> driver --> webdriver.Chrome(opts)
#
#     def click_on_reg_link(self):
#         # self.driver.find_element('link text', 'Register').click()
#         self.driver.find_element(*r_loc.reg_link).click()
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element('id', 'gender-male').click()
#         self.driver.find_element(*r_loc.gender_btn).click()
#
#     def enter_firstname(self, fname):
#         # self.driver.find_element('id', 'FirstName').send_keys(fname)
#         self.driver.find_element(*r_loc.firstname).send_keys(fname)
#
#     def enter_lastname(self, lname):
#         # self.driver.find_element('id', 'LastName').send_keys(lname)
#         self.driver.find_element(*r_loc.lastname).send_keys(lname)
#
#     def enter_reg_email(self, email):
#         # self.driver.find_element('id', 'Email').send_keys(email)
#         self.driver.find_element(*r_loc.reg_email).send_keys(email)
#
#     def enter_reg_pwd(self, pwd):
#         # self.driver.find_element('id', 'Password').send_keys(pwd)
#         self.driver.find_element(*r_loc.reg_pwd).send_keys(pwd)
#
#     def enter_confirm_pwd(self, pwd):
#         # self.driver.find_element('id', 'ConfirmPassword').send_keys(pwd)
#         self.driver.find_element(*r_loc.confirm_password).send_keys(pwd)

# ########################################################################################
#
'''
STEP6
'''
#
# from object_repository.reg_locators import RegisterLocators
#
# r_loc = RegisterLocators()
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
#
# class Register:
#
#     def __init__(self, driver):
#         self.driver = driver        ## self.driver --> driver --> webdriver.Chrome(opts)
#         self.wrap_obj = SeleniumWrapper(driver)
#
#     def click_on_reg_link(self):
#         # self.driver.find_element(*r_loc.reg_link).click()
#         self.wrap_obj.click_on_ele(r_loc.reg_link)
#
#     def click_on_gender_btn(self):
#         # self.driver.find_element(*r_loc.gender_btn).click()
#         self.wrap_obj.click_on_ele(r_loc.gender_btn)
#
#     def enter_firstname(self, fname):
#         # self.driver.find_element(*r_loc.firstname).send_keys(fname)
#         self.wrap_obj.enter_data(r_loc.firstname, fname)
#
#     def enter_lastname(self, lname):
#         # self.driver.find_element(*r_loc.lastname).send_keys(lname)
#         self.wrap_obj.enter_data(r_loc.lastname, lname)
#
#     def enter_reg_email(self, email):
#         # self.driver.find_element(*r_loc.reg_email).send_keys(email)
#         self.wrap_obj.enter_data(r_loc.reg_email, email)
#
#     def enter_reg_pwd(self, pwd):
#         # self.driver.find_element(*r_loc.reg_pwd).send_keys(pwd)
#         self.wrap_obj.enter_data(r_loc.reg_pwd, pwd)
#
#     def enter_confirm_pwd(self, pwd):
#         # self.driver.find_element(*r_loc.confirm_password).send_keys(pwd)
#         self.wrap_obj.enter_data(r_loc.confirm_password, pwd)
#

########################################################################################

'''
STEP6
'''

from object_repository.reg_locators import RegisterLocators
from generic_utilities.selenium_wrapper import SeleniumWrapper

r_loc = RegisterLocators()

class Register:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver --> webdriver.Chrome(opts)
        self.wrap_obj = SeleniumWrapper(driver)

    def click_on_reg_link(self):
        self.wrap_obj.click_on_ele(r_loc.reg_link)

    def click_on_gender_btn(self):
        self.wrap_obj.click_on_ele(r_loc.gender_btn)

    def enter_firstname(self, fname):
        self.wrap_obj.enter_data(r_loc.firstname, fname)

    def enter_lastname(self, lname):
        self.wrap_obj.enter_data(r_loc.lastname, lname)

    def enter_reg_email(self, email):
        self.wrap_obj.enter_data(r_loc.reg_email, email)

    def enter_reg_pwd(self, pwd):
        self.wrap_obj.enter_data(r_loc.reg_pwd, pwd)

    def enter_confirm_pwd(self, pwd):
        self.wrap_obj.enter_data(r_loc.confirm_password, pwd)












































































