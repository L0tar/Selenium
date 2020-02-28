from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    button = WebDriverWait(browser, 13).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element_by_css_selector('#book').click()
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_id('answer').send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_css_selector('#solve').click()

finally:
    time.sleep(5)
    browser.quit()
