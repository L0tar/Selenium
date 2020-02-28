from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
        browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(10)
    browser.quit()
