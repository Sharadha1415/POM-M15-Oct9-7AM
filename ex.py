# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get('')
#
# driver.find_element('xpath', '//tag@[attr="attr_value"]')
#
# ##------------------------------------------------------------------
#
# var = 'xpath', '//tag@[attr="attr_value"]'
#
# driver.find_element(var)
# driver.find_element(('xpath', '//tag@[attr="attr_value"]'))
#
# ##------------------------------------------------------------------
#
# var = 'xpath', '//tag@[attr="attr_value"]'
#
# driver.find_element(*var)
# driver.find_element(*('xpath', '//tag@[attr="attr_value"]'))
#
#
# ##------------------------------------------------------------------
#
# var = 'xpath', '//tag@[attr="attr_value"]'
#
# driver.find_element(*var)
# driver.find_element('xpath', '//tag@[attr="attr_value"]')


var = ('xpath', '//tag@[attr="attr_value"]')
print(var[0], type(var[0]))
print(var[1], type(var[1]))
















