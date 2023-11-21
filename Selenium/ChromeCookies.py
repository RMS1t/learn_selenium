from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
import time
import pickle
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import auth

options = webdriver.ChromeOptions()
useragent = UserAgent()
options.add_argument(
    f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://127.0.0.1:8000/accounts/login/?next=/catalog/")
    time.sleep(2)
    for cookie in pickle.load(open(f"{auth.login}_cookies", "rb")):
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.get('http://127.0.0.1:8000/')
    time.sleep(2)

    # username_input = driver.find_element(by=By.NAME, value='username')
    # username_input.clear()
    # username_input.send_keys(auth.login)
    #
    # password_input = driver.find_element(by=By.NAME, value='password')
    # password_input.clear()
    # password_input.send_keys(auth.password)
    # time.sleep(5)
    #
    # login_button =  driver.find_element(by=By.NAME, value='submit').click()
    # time.sleep(2)
    # pickle.dump(driver.get_cookies(), open(f"{auth.login}_cookies","wb"))


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
