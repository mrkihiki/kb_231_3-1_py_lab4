import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication

from Form5_ui import Ui_MainWindow as Form5_ui


def resource_path(relative_path):
    """Получает правильный путь к ресурсам для dev и exe"""
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Form5(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form5_ui()
        self.ui.setupUi(self)
        self.bool = True
        try:
            self.parent = args[-1]
        except:
            self.bool = False
        pixmap = QPixmap(resource_path(os.path.join('temp', 'nlo-t500x500.jpg')))
        if pixmap.isNull():
            pixmap = QPixmap("nlo-t500x500.jpg")
            if pixmap.isNull():
                raise Exception("Файл не найден")
        # Масштабируем изображение под размер метки с сохранением пропорций
        pixmap = pixmap.scaled(self.ui.label.width(),
                               self.ui.label.height(),
                               Qt.AspectRatioMode.KeepAspectRatio,
                               Qt.TransformationMode.SmoothTransformation)
        self.ui.label.setPixmap(pixmap)
        # Начальная позиция НЛО
        self.ufo_x = 340
        self.ufo_y = 250
        self.ufo_width = self.ui.label.width()
        self.ufo_height = self.ui.label.height()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Left:
            self.ufo_x -= 20
        if event.key() == Qt.Key.Key_Right:
            self.ufo_x += 20
        if event.key() == Qt.Key.Key_Up:
            self.ufo_y -= 20
        if event.key() == Qt.Key.Key_Down:
            self.ufo_y += 20
        self.nlo_move()

    def nlo_move(self):
        form_width = self.width()
        form_height = self.height()

        if self.ufo_x < -self.ufo_width:
            self.ufo_x = form_width
        elif self.ufo_x > form_width:
            self.ufo_x = -self.ufo_width
        if self.ufo_y < -self.ufo_height:
            self.ufo_y = form_height
        elif self.ufo_y > form_height:
            self.ufo_y = -self.ufo_height
        self.ui.label.move(self.ufo_x, self.ufo_y)

    def closeEvent(self, event):
        event.accept()  # Разрешаем закрытие
        if self.bool:
            self.parent.show()

def main():
    app = QApplication(sys.argv)
    ex = Form5()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()