import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/selects1.html")
browser.get("http://suninjuly.github.io/selects2.html")

try:
    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_element.text
    z = int(x) + int(y)
    time.sleep(1)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(z))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
