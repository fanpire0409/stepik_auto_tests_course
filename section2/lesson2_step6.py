import time
import math
from selenium import webdriver


def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))


browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

try:
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 150);")
    y_element = browser.find_element_by_css_selector('#answer')
    y_element.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
