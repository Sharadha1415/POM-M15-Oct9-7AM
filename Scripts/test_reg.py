import time
import pytest

# ## STEP3
#
# from POM.register import Register
#
# def test_demo_reg():
#     reg_obj = Register()
#     reg_obj.click_on_reg_link()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Harish')
#     reg_obj.enter_lastname('Chikkammanavar')
#     reg_obj.enter_reg_email('hari@gmail.com')
#     reg_obj.enter_reg_pwd('hari@12345')
#     reg_obj.enter_confirm_pwd('hari@12345')

# ###################################################################################
#
# ## STEP4
#
# from POM.register import Register
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
# def test_demo_reg():
#     reg_obj = Register()
#     reg_obj.click_on_reg_link()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Harish')
#     reg_obj.enter_lastname('Chikkammanavar')
#     reg_obj.enter_reg_email('hari@gmail.com')
#     reg_obj.enter_reg_pwd('hari@12345')
#     reg_obj.enter_confirm_pwd('hari@12345')

# ###################################################################################
#
# ## STEP5
#
# from POM.register import Register
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
# def test_demo_reg():
#     reg_obj = Register(driver)
#     reg_obj.click_on_reg_link()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Harish')
#     reg_obj.enter_lastname('Chikkammanavar')
#     reg_obj.enter_reg_email('hari@gmail.com')
#     reg_obj.enter_reg_pwd('hari@12345')
#     reg_obj.enter_confirm_pwd('hari@12345')

# ###################################################################################
#
# ## STEP5 only
# ## Defining the fixtures
#
# from POM.register import Register
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# ## setup --> driver = webdriver.Chrome(opts)
#
# def test_demo_reg(setup):
#     reg_obj = Register(setup)
#     reg_obj.click_on_reg_link()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Harish')
#     reg_obj.enter_lastname('Chikkammanavar')
#     reg_obj.enter_reg_email('hari@gmail.com')
#     reg_obj.enter_reg_pwd('hari@12345')
#     reg_obj.enter_confirm_pwd('hari@12345')
#

# ###################################################################################
#
# ## STEP5 only
# ## Defining the fixtures
#
# from POM.register import Register
#
# def test_demo_reg(setup):
#     reg_obj = Register(setup)
#     reg_obj.click_on_reg_link()
#     reg_obj.click_on_gender_btn()
#     reg_obj.enter_firstname('Harish')
#     reg_obj.enter_lastname('Chikkammanavar')
#     reg_obj.enter_reg_email('hari@gmail.com')
#     reg_obj.enter_reg_pwd('hari@12345')
#     reg_obj.enter_confirm_pwd('hari@12345')


###################################################################################

## STEP5 only
## read excel

from POM.register import Register
from generic_utilities.excel_utility import read_excel_data

path = r'C:\Users\Ramya\PycharmProjects\POM-M15-Oct9-7AM\external_files\data.xlsx'

reg_data = read_excel_data(path, 'reg')
## {'firstname': 'Harish', 'lastname': 'Chikkammanavar', 'reg_email': 'hari@gmail.com', 'reg_pwd': 'hari@12345', 'confirm_pwd': 'hari@12345'}


def test_demo_reg(setup):
    reg_obj = Register(setup)
    reg_obj.click_on_reg_link()
    reg_obj.click_on_gender_btn()
    reg_obj.enter_firstname(reg_data['firstname'])
    reg_obj.enter_lastname(reg_data['lastname'])
    reg_obj.enter_reg_email(reg_data['reg_email'])
    reg_obj.enter_reg_pwd(reg_data['reg_pwd'])
    reg_obj.enter_confirm_pwd(reg_data['confirm_pwd'])














