# Список опций https://peter.sh/experiments/chromium-command-line-switches/
from selenium import webdriver
from fake_useragent import UserAgent
import time
import random

# Список из user-agent
user_agents_list = [
    "Hello",
    "best",
    "python"
]
# Создаю объект класса user agent
useragent = UserAgent()

# Создаю объект опций
options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
options.add_argument(f"user-agent={useragent.random}") # Здесь же можно задать браузер

# Переменная для запросов
# url = "https://ru.wikipedia.org/"
# Переменная для браузера с которым будет производиться работа,
# в переменной создаем экземпляр класса webdriver в который основным параметром передаем абсолютный путь до драйвера
driver = webdriver.Chrome(
    executable_path="r'C:/Users/George Yulpatov/PyCharm Projects/Selenium/chromedriver",
    options=options
)
# Для Windows слэши нужно экранировать (из / сделать \\) либо добавить префикс r'

# Условия выполнения
try:
    # driver.get(url=url)
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    time.sleep(5)
    # driver.get_screenshot_as_file("wikipedia.png") # Скриншот

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
    driver.close()  # Метод закрытия
    driver.quit()  # Контрольный метод