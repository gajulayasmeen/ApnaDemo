#### Test case 1 ######
from selenium import webdriver
from selenium.webdriver import ActionChains

opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opt)
driver.get("https://d2csale.com/my-account/")
driver.maximize_window()
#
# driver.find_element('xpath','(//input[@placeholder="Username / Email"])[1]').send_keys("gajulayasmeen02@gmail.com")
# driver.find_element('xpath','(//input[@type="password"])[1]').send_keys("aman@786")
# driver.find_element('xpath','(//input[@type="checkbox"])[1]').click()
# driver.find_element('xpath','(//button[@type="submit"])[5]').click()


##### TestCase2 ####
#
# driver.find_element('xpath','(//input[@placeholder="Username / Email"])[1]').send_keys("gajulayasmeen02@gmail.com")
# driver.find_element('xpath','(//input[@type="password"])[1]').send_keys("aman@786")
# driver.find_element('xpath','(//input[@type="checkbox"])[1]').click()
# driver.find_element('xpath','(//button[@type="submit"])[5]').click()
#
# driver.find_element('id','thaps-search-autocomplete-2').send_keys("chains")
# driver.find_element('id','thaps-search-button').click()

###### TestCase3 #####

# driver.find_element('xpath','(//input[@placeholder="Username / Email"])[1]').send_keys("gajulayasmeen02@gmail.com")
# driver.find_element('xpath','(//input[@type="password"])[1]').send_keys("aman@786")
# driver.find_element('xpath','(//input[@type="checkbox"])[1]').click()
# driver.find_element('xpath','(//button[@type="submit"])[5]').click()
#
# driver.find_element('xpath',"(//span[text()='Fashion & Apparal'])[2]").click()


##### TestCase4 #####

# driver.find_element('xpath','(//input[@placeholder="Username / Email"])[1]').send_keys("gajulayasmeen02@gmail.com")
# driver.find_element('xpath','(//input[@type="password"])[1]').send_keys("aman@786")
# driver.find_element('xpath','(//input[@type="checkbox"])[1]').click()
# driver.find_element('xpath','(//button[@type="submit"])[5]').click()
#
# driver.find_element('xpath',"(//span[text()='Fashion & Apparal'])[2]").click()
#
# act_obj=ActionChains(driver)
# ele=driver.find_element('xpath','(//img[@loading="lazy"])[1]')
# act_obj.move_to_element(ele).perform()
# driver.find_element('xpath','(//a[text()="Add to cart"])[2]').click()


#### TestCase 5 #####
driver.find_element('xpath','(//input[@placeholder="Username / Email"])[1]').send_keys("gajulayasmeen02@gmail.com")
driver.find_element('xpath','(//input[@type="password"])[1]').send_keys("aman@786")
driver.find_element('xpath','(//input[@type="checkbox"])[1]').click()
driver.find_element('xpath','(//button[@type="submit"])[5]').click()

driver.find_element('xpath',"(//span[text()='Fashion & Apparal'])[2]").click()

act_obj=ActionChains(driver)
ele=driver.find_element('xpath','(//img[@loading="lazy"])[1]')
act_obj.move_to_element(ele).perform()
driver.find_element('xpath','(//a[text()="Add to cart"])[2]').click()
driver.find_element('xpath',"//div[text()='Proceed to Checkout']").click()
