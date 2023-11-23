from selenium import webdriver
# from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
import time
import pickle
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import auth

options = webdriver.ChromeOptions()
# useragent = UserAgent()
options.add_argument(
    f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://moodle.tomtit-tomsk.ru/login/index.php")
    time.sleep(2)

    username_input = driver.find_element(by=By.ID, value='username')
    username_input.clear()
    username_input.send_keys(auth.login)
    print("Input Login")

    password_input = driver.find_element(by=By.ID, value='password')
    password_input.clear()
    password_input.send_keys(auth.password)
    print("Input Password")

    login_button = driver.find_element(by=By.ID, value='loginbtn').click()
    print("Click Button")

    Name = driver.find_element(by=By.TAG_NAME, value='h2').text

    assert Name == 'С возвращением, Роман! 👋'
    print('Good name')
    url = "https://moodle.tomtit-tomsk.ru/my/courses.php"
    assert driver.current_url == url
    print('Good URL')
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
