from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(
    f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://127.0.0.1:8000/accounts/login/?next=/catalog/")
    driver.get_screenshot_as_png()

    username_input = driver.find_element(by=By.NAME, value='username')
    username_input.clear()
    username_input.send_keys('admin1')

    password_input = driver.find_element(by=By.NAME, value='password')
    password_input.clear()
    password_input.send_keys('admin1')
    time.sleep(5)

    login_button =  driver.find_element(by=By.NAME, value='submit').click()
    time.sleep(2)
    logout_button = driver.find_element(by=By.ID, value='logout').click()
    time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
