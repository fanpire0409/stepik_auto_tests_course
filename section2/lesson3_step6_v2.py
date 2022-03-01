from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    time.sleep(2)
    button1 = browser.find_element(By.XPATH, '//button')
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_value = browser.find_element(By.XPATH, "//*[@id = 'input_value']")
    x = x_value.text
    y = calc(x)
    y_value = browser.find_element(By.XPATH, "//*[@id = 'answer']")
    y_value.send_keys(y)
    button2 = browser.find_element(By.XPATH, '//button')
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
