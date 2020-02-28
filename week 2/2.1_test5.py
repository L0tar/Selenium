from selenium import webdriver
import time
import math


def calc(a):
    return str(math.log(abs(12*math.sin(int(a)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()
