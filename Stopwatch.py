import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import Qt, QTime, QTimer
class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.reset_button = QPushButton('Reset', self)
        self.time = QTime(0,0,0,0)
        self.timer = QTimer()
        self.time_label = QLabel("00:00:00.00",self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle('StopWatch')
        self.time_label.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)
        self.setStyleSheet("""
            QLabel,QPushButton {
                padding: 15px;
                margin: 10px;
                font-weight: bold;
            }
            QPushButton{
                background-color: hsl(350, 79%, 41%);
                font-size: 40px;
                border: 1px solid;
                border-radius: 10px;   
            }
            QPushButton:hover {
                background-color: hsl(350, 79%, 81%);
            }
            QLabel{
                background-color: hsl(192, 100%, 50%);
                font-size: 120px;
            }
        """)
        self.setLayout(vbox)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(StopWatch.time_format(self.time))
    def update(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(StopWatch.time_format(self.time))
    @staticmethod
    def time_format(time):
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}.{time.msec()//10:02}"


def main():
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()