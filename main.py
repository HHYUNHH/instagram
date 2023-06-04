import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QGroupBox, QLabel, QPlainTextEdit, QLineEdit, QRadioButton, QPushButton, QDesktopWidget, QApplication, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
import Common
from feed import feed
from highlight import highlight

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        
        self.toggle = True
        self.worker = Worker()
        self.worker.start()
        
        # self.worker.name.connect(self.prograss)
        self.worker.stop.connect(self.act_stop)
        
        self.initUI()
        
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setTextVisible(False)
        
        
        self.btn = QPushButton('Start')
        self.btn.clicked.connect(self.act)
        
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
        
        self.setWindowTitle('Instagram Photo&Video')
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
            view = 'on'
        elif self.qrb5.isChecked():
            view = 'off'
        
        return mode, view
    
    def act(self):
        if self.toggle:
            self.act_start()
        
        elif not self.toggle:
            self.act_stop()
    
    def act_start(self):
        self.toggle = False
        self.state(self.toggle)
        
        self.pbar.setMaximum(0)
        target_list = self.qte.toPlainText().split('\n')
        ID = self.qle1.text()
        PW = self.qle2.text()
        mode, view = self.check_radio()
        
        self.worker.act_start((target_list, ID, PW, mode, view))
        self.worker.start()
        
    def act_stop(self):
        self.toggle = True
        self.worker.act_stop()
        self.pbar.setMaximum(1)
        self.pbar.reset()
        self.state(self.toggle)
    
    def prograss(self, Str):
        self.pbar.text(Str)
    
    def state(self, Bool):
        self.btn.setText({True: "Start", False: "Stop"}[Bool])
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Worker(QThread):
    
    stop = pyqtSignal()
    # name = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.running = False
    
    def run(self):
        if self.running:
            self.instagram(self.target_list, self.ID, self.PW, self.mode, self.view)
            self.stop.emit()
    
    def driver_on(self, view):
        self.driver = Common.web(view)

    def act_start(self, INPUT):
        self.target_list, self.ID, self.PW, self.mode, self.view = INPUT
        self.running = True
        
    def act_stop(self):
        self.running = False
        try:
            self.driver.quit()
        except:
            pass
        
    def instagram(self, target_list, ID, PW, mode, view):

        self.driver = Common.web(view)
        self.driver.get('https://www.instagram.com')
        
        try:
            if Common.check_login(self.driver, ID, PW):
                print('로그인 실패')
                return
            
            for target in target_list:
                # self.name.emit(target)
                if mode in [1, 2]:
                    feed(self.driver, target)
                if mode in [1, 3]:
                    highlight(self.driver, target)
                print(target, '완료')
        except:
            print('페이지 로드 실패')
            return

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
   
# python ./instagram/main.py