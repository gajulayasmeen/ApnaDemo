####Challenge 1: Go to a long news article page (e.g., BBC, CNN).
# ○ Scroll down by 500 pixels using execute_script.
# ○ Scroll the page until a specific footer element is in view using arguments[0].scrollIntoView().
# ○ Take a screenshot of just the footer element (Selenium 4+).
# ○ Take a full-page screenshot.


from selenium import webdriver
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.bbc.com/")
driver.execute_script("window.scrollBy(0,500);")
ele=driver.find_element('xpath',"//a[text()='BritBox']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
#screenshot
ele.screenshot(r"C:\python_001\Selenium p\Screenshots\img2.png")
driver.save_screenshot(r"C:\python_001\Selenium p\Screenshots\totalPage.png")
driver.quit()





















