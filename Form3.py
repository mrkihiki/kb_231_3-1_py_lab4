import csv

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

from Form3_ui import Ui_MainWindow as Form3_ui


class Form3(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form3_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]

    def closeEvent(self, event):
        event.accept()  # Разрешаем закрытие
        self.parent.show()