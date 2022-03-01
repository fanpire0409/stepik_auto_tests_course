import time
import math
from selenium import webdriver


def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

try:
    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute("valuex")
    y = calc(int(x))
    y_element = browser.find_element_by_css_selector('input#answer')
    y_element.send_keys(y)
    time.sleep(1)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    time.sleep(1)
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
