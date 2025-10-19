import random

from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox

from Form4_ui import Ui_MainWindow as Form4_ui


class Form4(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form4_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.ui.pushButton.clicked.connect(lambda: QMessageBox.warning(
                self, '', ":(",
                QMessageBox.StandardButton.Ok))
        # Таймер для проверки положения курсора
        self.timer = self.startTimer(50)  # Проверка каждые 50ms

    def timerEvent(self, event):
        # Получаем позиции курсора и кнопки
        cursor_pos = QCursor.pos()
        button_pos = self.ui.pushButton.mapToGlobal(QPoint(0, 0))

        # Вычисляем расстояние между курсором и кнопкой
        distance = ((cursor_pos.x() - button_pos.x()) ** 2 +
                    (cursor_pos.y() - button_pos.y()) ** 2) ** 0.5

        # Если курсор близко к кнопке - перемещаем её
        if distance < 100:  # Дистанция 100 пикселей
            self.move_away_from_cursor(cursor_pos.x() - button_pos.x(), cursor_pos.y() - button_pos.y())

    def move_away_from_cursor(self, dx, dy):
        # Если расстояние равно 0, значит курсор находится прямо в центре кнопки
        # В этом случае мы выходим из функции, чтобы избежать деления на ноль
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance == 0:
            return

        # Увеличиваем скорость убегания когда курсор ближе
        speed_multiplier = 1.0 + (100 - distance) / 100
        current_speed = 8 * speed_multiplier

        # Вычисляем направление убегания
        move_x = -dx / distance * current_speed
        move_y = -dy / distance * current_speed

        # Получаем текущую позицию кнопки
        current_x = self.ui.pushButton.x()
        current_y = self.ui.pushButton.y()

        # Вычисляем новую позицию
        new_x = current_x + move_x
        new_y = current_y + move_y

        # Проверяем границы формы
        new_x = max(0, min(new_x, self.width() - self.ui.pushButton.width()))
        new_y = max(0, min(new_y, self.height() - self.ui.pushButton.height()))

        # Перемещаем кнопку
        self.ui.pushButton.move(int(new_x), int(new_y))

    def closeEvent(self, event):
        event.accept()  # Разрешаем закрытие
        self.parent.show()
