from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element_by_name("firstname").send_keys('Dsada')
    browser.find_element_by_name("lastname").send_keys('Pgfhj')
    browser.find_element_by_name("email").send_keys('jhgjl@kil.op')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'tefg.txt')
    browser.find_element_by_name('file').send_keys(file_path)
    browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(10)
    browser.quit()
