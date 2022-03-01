from selenium import webdriver
import time
import math

def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
    button1 = browser.find_element_by_css_selector('button.btn')
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_value = browser.find_element_by_css_selector('#input_value')
    x = x_value.text
    y = calc(x)
    y_value = browser.find_element_by_css_selector('#answer')
    y_value.send_keys(y)
    button2 = browser.find_element_by_css_selector('button.btn')
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
