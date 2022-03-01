import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/selects1.html")
browser.get("http://suninjuly.github.io/selects2.html")

try:
    x_element = browser.find_element_by_css_selector('#num1')
    x = x_element.text
    y_element = browser.find_element_by_css_selector('#num2')
    y = y_element.text
    z = int(x) + int(y)
    time.sleep(1)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(z))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
