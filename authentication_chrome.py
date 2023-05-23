from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
                     "36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    executable_path="r'C:/Users/George Yulpatov/PyCharm Projects/Selenium/chromedriver",
    options=options
)


try:
    driver.get("https://vk.com/")
    time.sleep(5)
# Заполнение поля логин
    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("89008585858")
    time.sleep(15)
# Заполнение поля пароль
    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    time.sleep(5)
# Нажатие на кнопку
    login_button = driver.driver.find_element_by_id("index_login_button").clik()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()