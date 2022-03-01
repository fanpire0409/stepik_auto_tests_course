from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x_input):
    return str(math.log(abs(12 * math.sin(int(x_input)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.XPATH, "//button[@id = 'book']")
    button.click()
    x_value = browser.find_element(By.XPATH, "//*[@id = 'input_value']")
    x = x_value.text
    y = calc(x)
    y_value = browser.find_element(By.XPATH, "//*[@id = 'answer']")
    y_value.send_keys(y)
    button2 = browser.find_element(By.XPATH, '//button[@id="solve"]')
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

