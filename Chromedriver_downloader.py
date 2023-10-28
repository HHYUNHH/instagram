import os, requests, re, zipfile, shutil, psutil
from urllib.request import urlretrieve


# 버전 비교용 함수
def ver_to_str(chrome_version):
    chrome_version = ''.join([x.zfill(4) for x in chrome_version.split('.')])
    return chrome_version

# 크롬드라이버 다운로더
def chromedriver_downloader():

    try:
        for proc in psutil.process_iter():
            if 'chromedriver' in proc.name().lower():
                proc.kill()
    except: pass

    # 크롬 버전 체크
    versions = [x.name for x in os.scandir("C:\\Program Files\\Google\\Chrome\\Application") if
                x.is_dir() and re.match("^[0-9.]+$", x.name)]
    if not versions: raise Exception('크롬 경로가 옳바르지 않습니다.')
    chrome_version = max(versions).rsplit('.', maxsplit=1)[0]

    # 버전에 맞는 드라이버 다운로드
    if ver_to_str('115.0.0') <= ver_to_str(chrome_version):
        url = f'https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_{chrome_version}'
    else:
        url = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version}'

    chrome_version = requests.get(url).text
    if 20 < len(chrome_version): raise Exception('호환 가능한 버전이 없습니다.')

    if ver_to_str('115.0.0.0') <= ver_to_str(chrome_version):
        url = f'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{chrome_version}/win32/chromedriver-win32.zip'
    else:
        url = f'https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip'


    # 압축 풀기 & 현재 경로로 파일 이동
    file_zip = './chromedriver.zip'
    urlretrieve(url, file_zip)
    fantasy_zip = zipfile.ZipFile(file_zip)
    fantasy_zip.extractall('./chromedriver/')
    fantasy_zip.close()
    if os.path.isfile('./chromedriver/chromedriver.exe'):
        file_path = './chromedriver/chromedriver.exe'
    else:
        file_path = './chromedriver/chromedriver-win32/chromedriver.exe'

    shutil.move(file_path, './chromedriver.exe')
    shutil.rmtree('./chromedriver/')
    os.remove(file_zip)