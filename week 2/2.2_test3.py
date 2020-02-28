from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    s = Select(browser.find_element_by_tag_name('select'))
    s.select_by_visible_text(str(int(x)+int(y)))
    browser.find_element_by_css_selector('.btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()
