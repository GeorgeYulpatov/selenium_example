# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent
from proxy_data import login, password
import time

# Переменная для браузера с которым будет производиться работа,
# в переменной создаем экземпляр класса webdriver в который основным параметром передаем абсолютный путь до драйвера
url = "https://ru.wikipedia.org/"
# Создаю объект класса user agent
useragent = UserAgent()

# Создаю объект опций
options = webdriver.FirefoxOptions()

# Добавление proxy
# proxy = "123.123.12.12:1000"
# firefox_capabilites = webdriver.DesiredCapabilities.FIREFOX # Доступ к возможностям браузера
# firefox_capabilites["marionette"] = True
#
# firefox_capabilites["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
#
# }

proxy_options = {
    "proxy": {
        "https": f"http://{login}: {password}@123.123.12.12:1000"
    }

}

# Перезапись useragent с помощью метода set_preference, можно задать свое значение в "useragent" или использовать
# useragent.random
options.set_preference("general.useragent.override", useragent.random)

# Переменная для запросов
driver = webdriver.Firefox(
    executable_path="C:/Users/George Yulpatov/PyCharm Projects/Selenium/Firefoxdriver",
    # options=options, proxy=proxy,
    seleniumwire_options=proxy_options
)
# Для Windows слэши нужно экранировать (из / сделать \\) либо добавить префикс r'

# Условия выполнения
try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    # time.sleep(5)

    # # Пример прямого перехода
    # driver.get(url="https://github.com/")
    # time.sleep(5)
    # driver.save_screenshot("github.png") # Скриншот
    # time.sleep(2)

    # Метод refresh - обновляет окно браузера
    # driver.refresh()

    driver.get("https://2ip.ru/")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close() # Метод закрытия
    driver.quit() # Контрольный метод
