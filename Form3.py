import random

from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QColor, QCursor, QPainter, QPolygonF
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

from Form3_ui import Ui_MainWindow as Form3_ui


class Form3(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form3_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.shapes = []

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Круг
            self.add_shape("circle", event.position())
        elif event.button() == Qt.MouseButton.RightButton:
            # Квадрат
            self.add_shape("square", event.position())

        self.update()  # Перерисовываем виджет

    def add_shape(self, shape_type, position):
        # Случайный цвет
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        # Случайный размер (от 20 до 80 пикселей)
        size = random.randint(20, 80)

        self.shapes.append({
            'type': shape_type,
            'x': position.x() - size / 2,  # Центрируем фигуру
            'y': position.y() - size / 2,
            'size': size,
            'color': color
        })

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            # Треугольник
            cursor_pos = self.mapFromGlobal(QCursor.pos())
            self.add_shape("triangle", cursor_pos)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for shape in self.shapes:
            painter.setBrush(shape['color'])

            if shape['type'] == 'circle':
                painter.drawEllipse(int(shape['x']), int(shape['y']),
                                    shape['size'], shape['size'])
            elif shape['type'] == 'square':
                painter.drawRect(int(shape['x']), int(shape['y']),
                                 shape['size'], shape['size'])
            elif shape['type'] == 'triangle':
                # Создаем треугольник
                half_size = shape['size'] / 2
                center_x = shape['x'] + half_size
                center_y = shape['y'] + half_size

                triangle = QPolygonF([
                    QPointF(center_x, center_y - half_size),  # Верхняя точка
                    QPointF(center_x - half_size, center_y + half_size),  # Левая нижняя
                    QPointF(center_x + half_size, center_y + half_size)  # Правая нижняя
                ])
                painter.drawPolygon(triangle)

    def closeEvent(self, event):
        event.accept()  # Разрешаем закрытие
        self.parent.show()
