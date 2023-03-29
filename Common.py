from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def web(view):
    view = view.lower()
    options = webdriver.ChromeOptions()
    if view == 'off':
        options.add_argument('headless') # 시각화 on/off
    elif view == 'on':
        options.add_argument('--user-data-dir=C:/Users/chois/AppData/Local/Google/Chrome/User Data/Profile 2')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--mute-audio')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36') # navigator.userAgent
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def check_login(driver, ID, PW):
    driver.implicitly_wait(5)
    tag = driver.find_elements(By.CSS_SELECTOR, '._aicz')
    
    if tag:
        tag[0].click()
        driver.implicitly_wait(5)
        tag = driver.find_elements(By.CSS_SELECTOR, '._aa4b')
        tag[0].send_keys(ID)
        tag[1].send_keys(PW)
        tag[1].send_keys(Keys.ENTER)

    driver.implicitly_wait(5)
    tag = driver.find_elements(By.CSS_SELECTOR, '.x78zum5.xurb0ha.x47corl')
    if tag:
        return False
    else:
        return True

# 주소 분석 후 이름, 확장자 리턴
def extract(Str):
    name = Str.split('?')[0].split('/')[-1]
    # name, extension = Str[0], Str[1]
    return name