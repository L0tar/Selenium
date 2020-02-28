from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_css_selector('.btn').click()
    all_windows = browser.window_handles
    new_window = all_windows[-1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(10)
    browser.quit()
