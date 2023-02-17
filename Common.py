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
    elif view != 'on':
        raise '인자값 에러'
    options.add_argument('--mute-audio')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36') # navigator.userAgent
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# 로그인
def login(driver, ID, PW):
    driver.implicitly_wait(10)
    tag = driver.find_elements(By.CSS_SELECTOR, '._acan')[1]
    tag.click()
    tag = driver.find_elements(By.CSS_SELECTOR, '._aa4b')
    tag[0].send_keys(ID)
    tag[1].send_keys(PW)
    tag[1].send_keys(Keys.ENTER)

# 로그인 확인
def check_login(driver):
    driver.implicitly_wait(10) 
    if not driver.find_elements(By.CSS_SELECTOR, '._ab16'):
        raise '로그인 실패'
    time.sleep(1)

# 주소 분석 후 이름, 확장자 리턴
def extract(Str):
    for extension in ['.jpg', '.mp4', '.webp', '.png']:
        if extension in Str:
            break

    name = Str.split(extension)[0].split('/')[-1]
    
    if extension != '.mp4':
        extension = '.jpg'
        
    return name+extension