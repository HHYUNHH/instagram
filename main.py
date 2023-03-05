import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QGroupBox, QLabel, QTextEdit, QLineEdit, QRadioButton, QPushButton, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt
from instagram_bot import instagram_bot

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Instagram Photo&Video')
        self.resize(500, 200)
        self.center()
        
        grid = QGridLayout()
        grid.addWidget(self.group_target(), 0, 0)
        grid.addWidget(self.group_login(), 0, 1)
        grid.addWidget(self.group_mode(), 1, 0)
        grid.addWidget(self.group_view(), 1, 1)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lb_state())
        vbox.addLayout(grid)
        vbox.addWidget(self.btn_play())
        self.setLayout(vbox)
        self.show()
    
    def group_target(self):
        groupbox = QGroupBox('Target')
        label = QLabel('ID:')
        self.qte = QTextEdit()
        
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
        self.qrb1 = QRadioButton('Pheed + Highlight')
        self.qrb2 = QRadioButton('Only Pheed')
        self.qrb3 = QRadioButton('Only Highlight')
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

    def btn_play(self):
        btn = QPushButton('Start')
        self.MSG = 'Progressing...'
        btn.clicked.connect(self.state_print)
        btn.released.connect(self.play_bot)
        return btn
    
    def lb_state(self):
        self.label = QLabel('Ready')
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        return self.label
    
    def state_print(self):
        MSG = self.MSG
        self.label.setText(MSG)
    
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
    
    def play_bot(self):
        target_list = self.qte.toPlainText().split('\n')
        ID = self.qle1.text()
        PW = self.qle2.text()
        mode, view = self.check_radio()
        try:
            instagram_bot(target_list, ID, PW, mode, view)
            self.MSG = 'Complete'
        except:
            self.MSG = 'Error'
        self.state_print()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())