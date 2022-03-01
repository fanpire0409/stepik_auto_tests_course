import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))


browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

try:
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 150);")
    y_element = browser.find_element(By.CSS_SELECTOR, '#answer')
    y_element.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
