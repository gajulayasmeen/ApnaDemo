###---------- ASSIGNMENT ------###########

# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()  #launching chrome browser
# driver.maximize_window()
# driver.get("https://practicetestautomation.com/practice-test-login/")
# driver.find_element('xpath','//input[@id="username"]').send_keys('student')
# driver.find_element('xpath','(//input[@id="username"]/ancestor::div[@id="form"]/descendant::input)[2]').send_keys('Password123')
# driver.find_element('xpath','(//input[@id="username"]/ancestor::div[@id="form"]/descendant::input)[2]/parent::div/following-sibling::button').click()
# sleep(3)




#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/followingsibling or preceding-sibling).
# ----------------------
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://the-internet.herokuapp.com/tables')
# print(driver.find_element("xpath",'//table[@id="table1"]/descendant::td[text()="jdoe@hotmail.com"]/following-sibling::td[2]').text)



###^^^^^^^^^^ CHALLENGE 2 ^^^^^^^^^^^^^^^^^^
# Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
# # --------------
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://the-internet.herokuapp.com/tables')
# driver.find_element("xpath",'//table[@id="table1"]/descendant::td[text()="Bach"]/following-sibling::td[5]/child::a[text()="delete"]')
# sleep(3)
# print(driver.find_element('xpath','//table[2]/descendant::td[text()="$100.00"]/ancestor::tr').text)
# sleep(2)
# driver.find_element('xpath','')



## ^^^^^^^ CHALLENGE 1 ^^^^^^^
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://the-internet.herokuapp.com/login')
# driver.find_element("xpath","//input[@id='username']").send_keys('student')
# driver.find_element('xpath','//input[@id="password"]').send_keys(('Password123'))
# driver.find_element('xpath',"//i[@class='fa fa-2x fa-sign-in']")





