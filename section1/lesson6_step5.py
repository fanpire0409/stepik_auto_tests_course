from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    link2 = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link2.click()

    input1 = browser.find_element_by_tag_name('input')
    # input1.send_keys("Ivan")
    input1.send_keys("Dara")
    input2 = browser.find_element_by_name('last_name')
    # input2.send_keys("Petrov")
    input2.send_keys("Rize")
    input3 = browser.find_element_by_class_name('city')
    # input3.send_keys("Smolensk")
    input3.send_keys("Blagoveschensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    time.sleep(2)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
