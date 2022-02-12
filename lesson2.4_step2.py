from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
# math.lol
    # return str(math.log(abs(12*math.sin(x))))
  

try: 

    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button=browser.find_element_by_id("book")
    button.click()

    time.sleep(1)

    x_element=browser.find_element_by_id("input_value")
    print ("x_element.text=",x_element.text)
    x=calc(x_element.text)
    print ("X=",x)
    answer=browser.find_element_by_id("answer")
    answer.send_keys(x)

    sbm=browser.find_element_by_id("solve")
    sbm.click()


    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()