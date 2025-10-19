import sys
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from start_ui import Ui_MainWindow as MainFormUI
from Form1 import Form1
from Form2 import Form2
from Form3 import Form3
from Form4 import Form4
#from Form5 import Form5
#from Form6 import Form6

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi('start_ui.py', self)  # Загружаем дизайн
        self.ui = MainFormUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.open_form(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.open_form(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.open_form(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.open_form(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.open_form(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.open_form(6))

    def open_form(self, form_number):
        if form_number == 1:
            self.form = Form1(self)
        elif form_number == 2:
            self.form = Form2(self)
        elif form_number == 3:
            self.form = Form3(self)
        elif form_number == 4:
            self.form = Form4(self)
        elif form_number == 5:
            self.form = Form5(self)
        elif form_number == 6:
            self.form = Form6(self)
        self.form.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())