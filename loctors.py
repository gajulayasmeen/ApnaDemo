import time
from selenium import webdriver
opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)
driver= webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
print(driver.title)
print(driver.current_url)



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# # LOCATORS
# driver.find_element('id','name').send_keys('Yasmeen')
# time.sleep(2)
# driver.find_element('id','name').send_keys('gajulayasmeen02@gmail.com')
# time.sleep(2)
# driver.find_element('id','phone').send_keys('8310359260')
#
# driver.close()



###########^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

import time
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options= opts)
# driver.maximize_window()
# driver.get(" https://the-internet.herokuapp.com/.")
#
# print(driver.title)
# driver.close()


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# import time
# import selenium
# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opts)
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# print(driver.title)
# driver.find_element('class_name','form-group')
# driver.find_element('id','female')
# driver.find_element('div','form-group')
# driver.sleep(3)
# driver.find_element('type','checkbox')
# driver.close()