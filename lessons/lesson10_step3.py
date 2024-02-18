import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока цена не станет 100 долларов
text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
browser.find_element(By.CSS_SELECTOR, "#book").click()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, '#answer')
input.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, "#solve").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()



