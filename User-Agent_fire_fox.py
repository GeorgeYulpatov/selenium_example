from selenium import webdriver
from fake_useragent import UserAgent
import time

# Переменная для браузера с которым будет производиться работа,
# в переменной создаем экземпляр класса webdriver в который основным параметром передаем абсолютный путь до драйвера
url = "https://ru.wikipedia.org/"
# Создаю объект класса user agent
useragent = UserAgent()

# Создаю объект опций
options = webdriver.FirefoxOptions()

# Перезапись useragent с помощью метода set_preference, можно задать свое значение в "useragent" или использовать
# useragent.random
options.set_preference("general.useragent.override", useragent.random)

# Переменная для запросов
driver = webdriver.Firefox(
    executable_path="C:/Users/George Yulpatov/PyCharm Projects/Selenium/Firefoxdriver",
    options=options
)
# Для Windows слэши нужно экранировать (из / сделать \\) либо добавить префикс r'

# Условия выполнения
try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    time.sleep(5)

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
