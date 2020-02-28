from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.execute_script("window.scrollBy(0, 100);")
    for s in ("#robotCheckbox", "#robotsRule", ".btn"):
        browser.find_element_by_css_selector(s).click()

finally:
    time.sleep(10)
    browser.quit()
