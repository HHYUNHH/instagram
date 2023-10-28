import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QPlainTextEdit, QLineEdit, QRadioButton, QPushButton, QDesktopWidget, QApplication, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal

import os, time, traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
from Chromedriver_downloader import chromedriver_downloader

class Instagram:

    def web(self, view=True):
        for i in os.listdir('C:/Users/'):
            path = f'C:/Users/{i}/AppData/Local/Google/Chrome/'
            if os.path.isdir(path):
                break
            path = 'C:/Users/Chrome/'
        path += f'User Data/Instagram'
        os.makedirs(path, exist_ok=True)

        options = Options()
        if not view:
            options.add_argument('headless')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument(f'--user-data-dir={path}')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
        options.add_argument('--mute-audio')
        options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
        service = Service(executable_path='./chromedriver.exe')

        try:
            self.driver = webdriver.Chrome(service=service, options=options)
        except:
            time.sleep(1)
            if os.path.isfile(path+'/Default/Preferences'):
                os.remove(path+'/Default/Preferences')
                options.add_argument(f'--user-data-dir={path}')
            chromedriver_downloader()
            self.driver = webdriver.Chrome(service=service, options=options)

    def end(self):
        try: self.driver.quit()
        except: pass

    def do_login(self, ID='', PW=''):
        
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get('https://www.instagram.com/')
        self.driver.implicitly_wait(15)
        tag = self.driver.find_elements(By.XPATH, '//*[@aria-label="Instagram"]')
        if not tag: raise Exception('다시 시도')
        
        self.driver.implicitly_wait(3)
        tag = self.driver.find_elements(By.XPATH, '//*[contains(text(), "로그인") or contains(text(), "Log in")]')
        if tag:
            webdriver.ActionChains(self.driver).move_to_element(tag[0]).click().perform()
            tag = self.driver.find_element(By.XPATH, '//*[contains(@name, "username")]')
            webdriver.ActionChains(self.driver).move_to_element(tag).click().send_keys(ID).perform()
            tag = self.driver.find_element(By.XPATH, '//*[contains(@name, "password")]')
            webdriver.ActionChains(self.driver).move_to_element(tag).click().send_keys(PW).perform()
            tag = self.driver.find_element(By.XPATH, '//*[contains(@type, "submit")]')
            webdriver.ActionChains(self.driver).move_to_element(tag).click().perform()

            for i in range(60):
                if self.driver.find_elements(By.XPATH, '//*[contains(@id, "loginForm")]'):
                    if i == 59: raise Exception('로그인 실패')
                    time.sleep(1)
                break

        tag = self.driver.find_elements(By.XPATH, '//*[contains(text(), "님으로 계속")]')
        if tag: webdriver.ActionChains(self.driver).move_to_element(tag[0]).click().perform()
        tag = self.driver.find_elements(By.XPATH, '//*[contains(text(), "정보 저장") or contains(text(), "Save Info")]')
        if tag: webdriver.ActionChains(self.driver).move_to_element(tag[0]).click().perform()
        tag = self.driver.find_elements(By.XPATH, '//*[contains(text(), "취소") or contains(text(), "Cancel")]')
        if tag: webdriver.ActionChains(self.driver).move_to_element(tag[0]).click().perform()

    def read_log(self, path):
        if os.path.isfile(path):
            with open(path, 'r', encoding='UTF8') as f:
                log_list = f.read().split('\n')
        else: log_list = []
        return log_list

    # 쿼리 벡터화
    def vac(self, Str):
        temp = 0
        vacdic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
        vacdic = {vacdic[idx]:idx+1 for idx in range(len(vacdic))}
        for idx, jdx in enumerate(Str[::-1]):
            temp += 100**(idx)*vacdic[jdx]
        return temp

    # 쿼리 정렬 함수
    def newsort(self, lst):
        sortlst = list()
        maxlen = len(max(lst, key=len))
        for idx in lst:
            jdx = idx.rjust(maxlen, 'A')
            sortlst.append([idx, self.vac(jdx)])
        sortlst = sorted(sortlst, key=lambda x: x[1])
        sortlst = [x[0] for x in sortlst]
        return sortlst

    # 저장
    def save_content(self, path, url):
        for i in range(2):
            try:
                name = url.split('?')[0].split('/')[-1].split('.')[0]
                if '-jpg_' in url: name+='.png'
                else: name+='.mp4'

                if not os.path.isfile(path+name):
                    urlretrieve(url, path+name)
                check = True
                break
            except: check = False
        return check

    def feed(self, username):
        path = f'./instagram/{username}/'
        os.makedirs(path, exist_ok=True)
        log_path = path+'log.txt'

        log_list = self.read_log(log_path)
        qrs_list = list()
        error_list = list()

        self.driver.implicitly_wait(5)
        for URL in (f'https://www.instagram.com/{username}', f'https://www.instagram.com/{username}/reels'):
            check_point = 0
            self.driver.get(URL)
            while self.driver.find_elements(By.XPATH, '//a[contains(@href, "/p/") or contains(@href, "/reel/")]'):
                tags = self.driver.find_elements(By.XPATH, '//a[contains(@href, "/p/") or contains(@href, "/reel/")]')
                for tag in tags:
                    qrs = tag.get_attribute('href').split('/')[-2]
                    if qrs in log_list:
                        if check_point == 3: break
                        check_point+=1
                    elif qrs not in qrs_list:
                        qrs_list.append(qrs)

                if check_point == 3: break
                webdriver.ActionChains(self.driver).move_to_element(tag).perform()
                time.sleep(2+(len(qrs_list)//250))
                if tag == self.driver.find_elements(By.XPATH, '//a[contains(@href, "/p/") or contains(@href, "/reel/")]')[-1]: break

        if qrs_list:
            qrs_list = self.newsort(qrs_list)
        else: return

        for qrs in qrs_list:

            url_list = list()
            self.driver.get(f'https://www.instagram.com/p/{qrs}')
            self.driver.implicitly_wait(5)
            while True:
                tags = self.driver.find_elements(By.XPATH, '//*[contains(@style, "cover;") or contains(@src, ".mp4") and not(contains(@src, "data:") and contains(@src, "blob:"))]')
                if not tags: raise Exception('연결 확인')
                for tag in tags:
                    url = tag.get_attribute('src')
                    if url in url_list: continue
                    url_list.append(url)
                
                webdriver.ActionChains(self.driver).move_to_element(tag).perform()
                if tag == self.driver.find_elements(By.XPATH, '//*[contains(@style, "cover;") or contains(@src, ".mp4") and not(contains(@src, "data:") and contains(@src, "blob:"))]')[-1]: break
                
            check = True
            for url in url_list:
                if not self.save_content(path, url):
                    check = False
                    error_list.append(url)

            if check:
                with open(log_path, 'a', encoding='UTF8') as f:
                    log_list = f.write(qrs+'\n')
                    
        if error_list: print('\n'.join(error_list))

    def highlights(self, username):
        self.driver.get(f'https://www.instagram.com/{username}')
        self.driver.implicitly_wait(5)
        tags = self.driver.find_elements(By.XPATH, '//*[contains(@role, "menuitem")]')
        if not tags: return
        path = f'./instagram/{username}/highlights/'
        os.makedirs(path, exist_ok=True)
        webdriver.ActionChains(self.driver).move_to_element(tags[0]).click().perform()

        for idx in range(10):
            while 'highlights' in self.driver.current_url:
                tag = self.driver.find_element(By.XPATH, '//*[contains(@src, "dst-jpg_e35") or contains(@src, ".mp4") and not(contains(@src, "data:") and contains(@src, "blob:"))]')
                url = tag.get_attribute('src')
                group = self.driver.current_url.split('highlights/')[-1]
                os.makedirs(path+group, exist_ok=True)
                if not self.save_content(path+group, url): print(url)
                tags = self.driver.find_elements(By.XPATH, '//div[contains(@role, "button")]//button')
                webdriver.ActionChains(self.driver).move_to_element(tags[-1]).click().perform()
            time.sleep(1)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        
        self.toggle = True
        self.worker = Worker()
        self.worker.start()
        
        # self.worker.name.connect(self.prograss)
        self.worker.stop.connect(self.stop)
        
        self.initUI()
        
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setTextVisible(False)
        
        self.btn = QPushButton('Start')
        self.btn.clicked.connect(self.work)
        
        grid = QGridLayout()
        grid.addWidget(self.group_target(), 0, 0)
        grid.addWidget(self.group_login(), 0, 1)
        grid.addWidget(self.group_mode(), 1, 0)
        grid.addWidget(self.group_view(), 1, 1)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.pbar)
        vbox.addLayout(grid)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        self.show()
        
        self.setWindowTitle('Instagram Media Downloader')
        self.resize(500, 200)
        self.center()
    
    def group_target(self):
        groupbox = QGroupBox('Target')
        label = QLabel('ID:')
        self.qte = QPlainTextEdit()
        
        grid = QGridLayout()
        grid.addWidget(label, 0, 0)
        grid.addWidget(self.qte, 0, 1)
        groupbox.setLayout(grid)
        
        return groupbox
        
    def group_login(self):
        groupbox = QGroupBox('Login')
        label1 = QLabel('ID:')
        label2 = QLabel('PW:')
        self.qle1 =QLineEdit()
        self.qle2 =QLineEdit()
        
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.qle1, 0, 1)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(self.qle2, 1, 1)
        groupbox.setLayout(grid)
        
        return groupbox
        
    def group_mode(self):
        groupbox = QGroupBox('Mode')
        self.qrb1 = QRadioButton('Feed + Highlight')
        self.qrb2 = QRadioButton('Feed')
        self.qrb3 = QRadioButton('Highlight')
        self.qrb1.setChecked(True)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.qrb1)
        vbox.addWidget(self.qrb2)
        vbox.addWidget(self.qrb3)
        groupbox.setLayout(vbox)
        
        return groupbox
        
    def group_view(self):
        groupbox = QGroupBox('View')
        self.qrb4 = QRadioButton('On')
        self.qrb5 = QRadioButton('Off')
        self.qrb4.setChecked(True)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.qrb4)
        vbox.addWidget(self.qrb5)
        groupbox.setLayout(vbox)
        
        return groupbox
    
    def check_radio(self):
        if self.qrb1.isChecked():
            mode = 1
        elif self.qrb2.isChecked():
            mode = 2
        elif self.qrb3.isChecked():
            mode = 3
        
        if self.qrb4.isChecked():
            view = True
        elif self.qrb5.isChecked():
            view = False
        
        return mode, view
    
    def work(self):
        if self.toggle:
            self.btn.setText('Stop')
            self.toggle = False
            self.pbar.setMaximum(0)

            username_list = self.qte.toPlainText().split('\n')
            ID = self.qle1.text()
            PW = self.qle2.text()
            mode, view = self.check_radio()

            self.worker.resume(username_list, ID, PW, mode, view)
            self.worker.start()
        
        elif not self.toggle:
            self.toggle = True
            self.btn.setText('Start')
            self.worker.pause()
    
    def stop(self):
        self.toggle = True
        self.btn.setText('Start')
        self.pbar.setMaximum(1)
        self.pbar.reset()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Worker(QThread):
    
    stop = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.running = False
    
    def run(self):

        if self.running:
            try:
                self.TEST = Instagram()
                self.TEST.web(self.view)
                self.TEST.do_login(self.ID, self.PW)

                for username in self.username_list:
                    if not username: continue
                    if self.mode in (1, 2) and self.running:
                        self.TEST.feed(username)
                    if self.mode in (1, 3) and self.running:
                        self.TEST.highlights(username)
            
            except: pass
            self.pause()

    def resume(self, username_list, ID, PW, mode, view):
        self.username_list, self.ID, self.PW, self.mode, self.view = username_list, ID, PW, mode, view
        self.running = True

    def pause(self):
        self.running = False
        self.TEST.end()
        self.stop.emit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())