from selenium import webdriver
import time
import random

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys(''.join(map(str, [random.randrange(10) for _ in range(random.randrange(1, 10))])))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
