import sys, time
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QTextEdit,QVBoxLayout,QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
class PBT(QThread):
    def __init__(self,mainwindow,parent = None):
        super().__init__()
        self.mainw = mainwindow

    def run(self):
        value = 0
        while value < 100:
            value += 1
            self.mainw.progressbar.setValue(value)
            time.sleep(0.2)

class MPBW(QDialog):
    def __init__(self):
        super().__init__()
        self.progressbar = QProgressBar()
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.Pushbtn = QPushButton('Start')
        self.Pushbtn.clicked.connect(self.start)
        self.TextEd = QTextEdit()
        self.setGeometry(300,400,300,150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.Pushbtn)
        vbox.addWidget(self.TextEd)
        vbox.addWidget(self.progressbar)
        self.setLayout(vbox)

        self.new_class = PBT(self)

    def start(self):
        self.new_class.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MPBW()
    main.show()
    sys.exit(app.exec_())