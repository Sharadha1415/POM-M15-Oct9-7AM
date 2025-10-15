# import pytest
# import time
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

###############################################################################################

import pytest
import time

from selenium import webdriver
from generic_utilities.property_utility import property_data

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

property_ = property_data()  ## {'browser': 'chrome', 'url': 'https://demowebshop.tricentis.com/'}


@pytest.fixture()
def setup():
    if property_['browser'] == 'chrome':
        driver = webdriver.Chrome(opts)
    elif property_['browser'] == 'firefox':
        driver = webdriver.Firefox()
    elif property_['browser'] == 'edge':
        driver = webdriver.Edge()

    driver.get(property_['url'])
    time.sleep(2)
    yield driver
    driver.close()