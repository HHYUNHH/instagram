from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import time, os
from Common import extract

# 로그파일 로드
def log_load(PATH):
    if os.path.isfile(PATH):
        f = open(PATH, 'r')
        log_list = (f.read().split('\n'))
        f.close()
    else:
        log_list = []
    
    return log_list

# 포스트 로드 확인
def check_post(driver):
    check_count = 0
    while True:
        try:
            driver.implicitly_wait(5)
            driver.find_element(By.CSS_SELECTOR, '._aatk')
            break
        except:
            driver.refresh()
            if check_count == 2:
                raise '페이지 로드 실패'
            check_count += 1

# 피드 탐색
def collect_qrs(driver, target, log_list):
    check_count = 0
    dic = {
        'general' :['', '._aabd', []],
        'reels' : ['/reels', '._aajw', []]
        }
    for pheed in dic:
        old = 0
        driver.get('https://www.instagram.com/' + target + dic[pheed][0])
        while True:
            time.sleep(1)
            driver.implicitly_wait(5)
            tag = driver.find_elements(By.CSS_SELECTOR, f'{dic[pheed][1]} .x1i10hfl')
            for i in tag:
                qrs = i.get_attribute('href').split('/')[-2]
                if qrs not in dic[pheed][2] + dic['general'][2]:
                    if qrs in log_list:
                        if check_count == 3:
                            old = len(dic[pheed][2])
                            break
                        check_count += 1
                        continue
                    dic[pheed][2].append(qrs)
            
            if old == len(dic[pheed][2]):
                break
            
            old_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if old_height == new_height:
                time.sleep(1)
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                
            old = len(dic[pheed][2])
            
    return dic

# 포스트 내 데이터 링크 수집
def colect_link_within_post(driver, link_list):
    for css in ['._aagu._aato img.x5yr21d', '._aato ._ab1d', 'video.x1lliihq']:
        driver.implicitly_wait(0.2)
        tag = driver.find_elements(By.CSS_SELECTOR, css)
        for i in tag:
            link = i.get_attribute('src')
            if link in link_list:
                continue
            link_list.append(link)
            
    return link_list

# 포스트 탐색
def read_post(driver):
    link_list = []
    check_count = 0
    while True:
        link_list = colect_link_within_post(driver, link_list)
        
        try:
            driver.implicitly_wait(0.2)
            driver.find_element(By.CSS_SELECTOR, '._ab8w ._afxw').click()
            continue
        except:
            if check_count == 3:
                raise '페이지 로드 실패'
            # NoneType 에러 방지
            if None in link_list or not link_list:
                driver.refresh()
                link_list.clear()
                time.sleep(5)
                check_count += 1
                continue
            
            return link_list

# 데이터저장 + 로그기록
def save_media(driver, output_path, link_list, qrs, log_path):
    for link in link_list:
        try:
            urlretrieve(link, f'{output_path}/{extract(link)}')
        except:
            try:
                driver.implicitly_wait(0.5)
                tag = driver.find_element(By.XPATH, '//meta[@property="og:video:secure_url"]')
                link = tag.get_attribute('content')
                urlretrieve(link, f'{output_path}/{extract(link)}')
            except:
                print('저장 하지 못한 포스트:', qrs)
                qrs = 0
    if qrs:
        f = open(log_path, 'a')
        f.write(f'{qrs}\n')
        f.close()
        
#
def pheed(driver, target):
    output_path = f'./instagram/{target}'
    log_path = f'{output_path}/log.txt'
    os.makedirs(output_path, exist_ok=True)
    
    log_list = log_load(log_path)

    pheed_type = collect_qrs(driver, target, log_list)
    
    for qrs_list in [pheed_type['general'][2], pheed_type['reels'][2]]:
        
        for qrs in qrs_list[::-1]:
            
            if qrs in log_list:
                continue
            
            driver.get('https://www.instagram.com/p/' + qrs)

            check_post(driver)
            
            link_list = read_post(driver)
            
            save_media(driver, output_path, link_list, qrs, log_path)