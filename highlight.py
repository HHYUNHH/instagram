from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import os
from Common import extract

# 하이라이트 유무 확인
def check_highlight(driver):
    driver.implicitly_wait(5)
    tag = driver.find_elements(By.CSS_SELECTOR, '._aams')[0]
    tag.click()

# 하이라이트 로드 확인
def check_highlight_load(driver, s):
    driver.implicitly_wait(s)
    driver.find_element(By.CSS_SELECTOR, '._afhn')

def colect_link_within_highlight(driver):
    tag = []
    for css in ['video.x1lliihq', 'img._aa63']:#'video source'
        driver.implicitly_wait(0.1)
        tag.extend(driver.find_elements(By.CSS_SELECTOR, css))
    return tag

def highlight(driver, target):
    output_path = f'./instagram/{target}/highlight'
    os.makedirs(output_path, exist_ok=True)
    log_list = os.listdir(output_path)
    driver.get('https://www.instagram.com/' + target)
    
    try:
        check_highlight(driver)
    except:
        return None
    
    check_highlight_load(driver, 10)
    
    while True:
        try:
            check_highlight_load(driver, 0.1)
        except:
            break
        
        tag = colect_link_within_highlight(driver)
        
        if not tag:
            continue
        
        link = tag[0].get_attribute('src')
        file = extract(link)
        if not file in log_list:
            urlretrieve(link, f'{output_path}/{file}')
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR, 'button._aafj').click()
                break
            except:
                pass