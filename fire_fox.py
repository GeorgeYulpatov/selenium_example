from selenium import webdriver
import time

# Переменная для браузера с которым будет производиться работа,
# в переменной создаем экземпляр класса webdriver в который основным параметром передаем абсолютный путь до драйвера

url = "https://ru.wikipedia.org/"
# Переменная для запросов
driver = webdriver.Firefox(executable_path="C:/Users/George Yulpatov/PyCharm Projects/Selenium/Firefoxdriver")
# Для Windows слэши нужно экранировать (из / сделать \\) либо добавить префикс r'

# Условия выполнения
try:
    driver.get(url=url)
    time.sleep(5)
    # driver.get_screenshot_as_file("wiki_mozilla.png")  # Скриншот

    # # Пример прямого перехода
    # driver.get(url="https://github.com/")
    # time.sleep(5)
    # driver.save_screenshot("github.png") # Скриншот
    # time.sleep(2)

    # Метод refresh - обновляет окно браузера
    # driver.refresh()
except Exception as ex:
    print(ex)
finally:
    driver.close() # Метод закрытия
    driver.quit() # Контрольный метод
