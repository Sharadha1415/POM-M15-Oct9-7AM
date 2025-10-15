import time

import pytest

# ## STEP3 execution
#
# from POM.login import Login
#
# def test_demo_login():
#     login_obj = Login()
#     login_obj.click_on_login_link()
#     login_obj.enter_login_email('hari@gmail.com')
#     login_obj.enter_login_pwd('hari@12345')

# ##################################################################################
#
# ## STEP4
#
# from POM.login import Login
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
# def test_demo_login():
#     login_obj = Login()
#     login_obj.click_on_login_link()
#     login_obj.enter_login_email('hari@gmail.com')
#     login_obj.enter_login_pwd('hari@12345')


# ##################################################################################
#
# ## STEP5
#
# from POM.login import Login
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
# def test_demo_login():
#     login_obj = Login(driver)
#     login_obj.click_on_login_link()
#     login_obj.enter_login_email('hari@gmail.com')
#     login_obj.enter_login_pwd('hari@12345')

# ##################################################################################
#
# ## STEP5
#
# from POM.login import Login
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
# def test_demo_login(setup):
#     login_obj = Login(setup)
#     login_obj.click_on_login_link()
#     login_obj.enter_login_email('hari@gmail.com')
#     login_obj.enter_login_pwd('hari@12345')
#

# ##################################################################################
#
# ## STEP5
#
# from POM.login import Login
#
# def test_demo_login(setup):
#     login_obj = Login(setup)
#     login_obj.click_on_login_link()
#     login_obj.enter_login_email('hari@gmail.com')
#     login_obj.enter_login_pwd('hari@12345')
#

##################################################################################

## STEP5

from POM.login import Login
from generic_utilities.excel_utility import read_excel_data

path = r'C:\Users\Ramya\PycharmProjects\POM-M15-Oct9-7AM\external_files\data.xlsx'
login_data = read_excel_data(path, 'login')
# print(login_data)           ## {'login_email': 'hari@gmail.com', 'login_pwd': 'hari@12345'}

def test_demo_login(setup):
    login_obj = Login(setup)
    login_obj.click_on_login_link()
    login_obj.enter_login_email(login_data['login_email'])
    login_obj.enter_login_pwd(login_data['login_pwd'])

















