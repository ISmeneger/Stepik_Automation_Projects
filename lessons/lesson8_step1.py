from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def summa(x, y):
    return int(x) + int(y)

link = 'https://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.CSS_SELECTOR, '#num1')
x = x.text
y = browser.find_element(By.CSS_SELECTOR, '#num2')
y = y.text
summ = summa(x, y)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summ)) # ищем элемент со значением суммы

browser.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(10)