import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
    СКРОЛЛ ВНИЗ, ВВОД ТЕКСТА В ПОЛЕ, НАЖАТИЕ РАДИОБАТОН, ЧЕКБОКС И КНОПКИ
"""
# Открыть страницу https://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

# try:
#     # Открыть страницу https://SunInJuly.github.io/execute_script.html.
#     # Считать значение для переменной x.
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # Считать значение для переменной x.
#     x = browser.find_element(By.ID, "input_value").text
#     # Посчитать математическую функцию от x.
#     y = str(math.log(abs(12*math.sin(int(x)))))
#     # Проскроллить страницу вниз.
#     browser.execute_script("window.scrollBy(0, 120);")
#     # Ввести ответ в текстовое поле.
#     input_1 = browser.find_element(By.ID, "answer").send_keys(y)
#     # Выбрать checkbox "I'm the robot".
#     chekbox = browser.find_element(By.ID, "robotCheckbox").click()
#     # Переключить radiobutton "Robots rule!"
#     radiobutton = browser.find_element(By.ID, "robotsRule").click()
#     # Нажать на кнопку "Submit" 
#     button = browser.find_element(By.TAG_NAME, "button")
#     time.sleep(1)
#     button.click()
    
# finally:
#     time.sleep(10)
#     browser.quit()
    
    
import os 
# конструкция ниже позволяет переносить папку в другую директорию или компьютер без ущерба работоспособности
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir,'file.txt')           # добавляем к этому пути имя файла 
# element.send_keys(file_path)
# file = open('languages.txt', 'r', encoding='utf-8')

# languages = file.readlines()

# file.close()
# # print(languages)
'''
ЗАГРУЗКА ФАЙЛА
'''
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

# try:
#     # Открыть страницу http://suninjuly.github.io/file_input.html
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # Заполнить текстовые поля: имя, фамилия, email
#     input1 = browser.find_element(By.NAME, "firstname")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "lastname")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.NAME, "email")
#     input3.send_keys("ivan_petrov@fmail.com")
#     # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#     current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#     file_path = os.path.join(current_dir,'resume.txt')           # добавляем к этому пути имя файла 
#     element = browser.find_element(By.ID, "file")
#     element.send_keys(file_path)
#     # Нажать на кнопку "Submit" 
#     button = browser.find_element(By.TAG_NAME, "button")
#     time.sleep(1)
#     button.click()

# finally:
#     time.sleep(10)
#     browser.quit()
    
"""АЛЕРТ КОНФИРМ ВВОД ИНФОРМАЦИИ"""
'''
window = browser.switch_to.alert
window.accept() # принять
window.dismiss() # отклонить
window.send_keys("text").accept() # ввести текст и принять
'''

#Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

# try:
#     # Открыть страницу http://suninjuly.github.io/alert_accept.html
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # Нажать на кнопку
#     button = browser.find_element(By.TAG_NAME, "button").click()
#     # Принять confirm
#     confirm = browser.switch_to.alert.accept()
#     # На новой странице решить капчу для роботов, чтобы получить число с ответом
#     x = browser.find_element(By.ID, "input_value").text
#     y = str(math.log(abs(12*math.sin(int(x)))))
#     input1 = browser.find_element(By.ID, "answer").send_keys(y)
#     # Нажать на кнопку "Submit"
#     button = browser.find_element(By.TAG_NAME, "button").click()
    
# finally:
#     time.sleep(10)
#     browser.quit()
    
'''
ПЕРЕХОД НА НОВУЮ ВКЛАДКУ БРАУЗЕРА

browser.switch_to.window(window_name)
new_window = browser.window_handles[1] # имя второй вкладки
first_window = browser.window_handles[0] # имя первой вкладки

'''

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

# try:
#     link = 'http://suninjuly.github.io/redirect_accept.html'
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # Нажать на кнопку
#     button = browser.find_element(By.TAG_NAME, "button").click()
#     # Переключиться на новую вкладку
#     new_window = browser.window_handles[1] # имя второй вкладки
#     first_window = browser.window_handles[0] # имя первой вкладки
#     browser.switch_to.window(new_window)
#     # Пройти капчу для робота и получить число-ответ
#     x = browser.find_element(By.ID, "input_value").text
#     y = str(math.log(abs(12*math.sin(int(x)))))
#     input1 = browser.find_element(By.ID, "answer").send_keys(y)
#     # Нажать на кнопку "Submit"
#     button = browser.find_element(By.TAG_NAME, "button").click()
# finally:
#     time.sleep(10)
#     browser.quit()
    
'''
ЗАДЕРКА ВЗАИМОДЕЙСТВИЯ С ЭЛЕМЕНТАМИ

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
'''

"""
ИСКЛЮЧЕНИЯ WebDriver
Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.

Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение. 

Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.   

NoSuchElementException - нет такого вообще
StaleElementReferenceException -  был элемент да сплыл
ElementNotVisibleException - видишь элемент? И я не вижу, а он есть.

"""
try:
    link='http://suninjuly.github.io/cats.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    browser.find_element(By.ID, "button")
except Exception as e:
    print('-' * 30)
    print("Произошло исключение:", str(e))
    print('-' * 30)
finally:
    time.sleep(3)
    browser.quit()