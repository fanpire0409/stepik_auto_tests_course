import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

try:
    x_element = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    y_element.send_keys(y)
    time.sleep(1)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    time.sleep(1)
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
