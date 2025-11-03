import os
import sys
import base64

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QSpinBox, QWidget, \
    QVBoxLayout, QLabel

from Form6_1_ui import Ui_MainWindow as Form6_1_ui
from Form6_2 import Form6_2

def resource_path(relative_path):
    """Получает правильный путь к ресурсам для dev и exe"""
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Form6_1(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form6_1_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.bool = True
        self.sort_item = 0
        self.ui.pushButton_3.clicked.connect(lambda: self.run(1))
        self.ui.pushButton.clicked.connect(lambda: self.run(2))
        self.ui.pushButton_4.clicked.connect(lambda: self.run(3))
        self.ui.pushButton_2.clicked.connect(lambda: self.run(4))
        self.select_data()

    def run(self, form_number):
        #cursor = self.parent.connection.cursor()
        if form_number == 1:
            self.bool_new = True
            self.form6_2 = Form6_2(self)
            self.form6_2.show()
            self.bool = False
            self.close()
        elif form_number == 2:
            self.bool_new = False
            self.form6_2 = Form6_2(self)
            self.form6_2.show()
            self.bool = False
            self.close()
        elif form_number == 3:
            id = self.ui.spinBox.text()
            if id not in [str(item[0]) for item in self.res]:
                return
            # Спрашиваем у пользователя подтверждение на удаление элемента
            valid = QMessageBox.question(
                self, '', "Действительно удалить элемент с id " + id,
                QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
            # Если пользователь ответил утвердительно, удаляем элемент.
            # Не забываем зафиксировать изменения
            if valid == QMessageBox.StandardButton.Yes:
                cur = self.parent.connection.cursor()
                cur.execute("DELETE FROM books WHERE id = ?", (id,))
                self.parent.connection.commit()
                self.select_data()
        elif form_number == 4:
            if self.ui.comboBox.currentText() == "":
                self.select_data()
            elif self.ui.comboBox.currentText() == "автор":
                for row in range(self.ui.tableWidget.rowCount()):
                    item = self.ui.tableWidget.item(row, 2)
                    if item is not None:
                        item_text = item.text().lower()
                        # Скрываем строку, если текст не найден
                        self.ui.tableWidget.setRowHidden(row, self.ui.lineEdit.text().lower() not in item_text)
            elif self.ui.comboBox.currentText() == "название":
                for row in range(self.ui.tableWidget.rowCount()):
                    item = self.ui.tableWidget.item(row, 1)
                    if item is not None:
                        item_text = item.text().lower()
                        # Скрываем строку, если текст не найден
                        self.ui.tableWidget.setRowHidden(row, self.ui.lineEdit.text().lower() not in item_text)


    @staticmethod
    def blob_to_pixmap(blob_data):
        """Конвертирует BLOB в QPixmap"""
        try:
            # Если blob_data - строка, конвертируем в байты
            if isinstance(blob_data, str):
                blob_data = blob_data.encode('latin-1')

            pixmap = QPixmap()
            pixmap.loadFromData(blob_data)
            return pixmap
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
            return QPixmap()

    # @staticmethod
    # def save_blob_to_file(blob_data, file_path="temp.jpg"):
    #     """
    #     Сохраняет BLOB данные как файл изображения
    #
    #     Args:
    #         blob_data: данные из базы
    #         file_path: путь для сохранения
    #     """
    #     try:
    #         if blob_data:
    #             with open(file_path, 'wb') as file:
    #                 file.write(blob_data)
    #             print(f"Изображение сохранено: {file_path}")
    #             return True
    #         else:
    #             print("Нет данных для сохранения")
    #             return False
    #     except Exception as e:
    #         print(f"Ошибка сохранения: {e}")
    #         return False

    def select_data(self):
        # Получим таблицу
        query = "SELECT * FROM books"
        self.res = self.parent.connection.cursor().execute(query).fetchall()
        names = [item[0] for item in
                 self.parent.connection.cursor().execute(
                     "SELECT name FROM pragma_table_info('books')").fetchall()]
        # Заполним размеры таблицы
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels(names)
        # Заполняем таблицу элементами
        ii = -1
        for i, row in enumerate(self.res):
            ii += 1
            self.ui.tableWidget.setRowCount(
                self.ui.tableWidget.rowCount() + 1)
            jj = 0
            for j, elem in enumerate(row):
                if j == 0:
                    self.ui.tableWidget.setItem(
                        ii, jj, QTableWidgetItem(str(ii + 1)))
                elif j!=5:
                    self.ui.tableWidget.setItem(ii, jj, QTableWidgetItem(str(elem)))
                else:
                    # print(elem)
                    # x= base64.b64decode(elem.encode('utf-8'))
                    # if self.save_blob_to_file(base64.b64decode(elem.encode('utf-8'))):
                    #      print("e")
                    pixmap = QPixmap(self.blob_to_pixmap(base64.b64decode(elem.encode('utf-8'))))
                    if not pixmap.isNull():
                        # Масштабируем изображение (PyQt6)
                        pixmap = pixmap.scaled(100, 150,
                                               Qt.AspectRatioMode.KeepAspectRatio,
                                               Qt.TransformationMode.SmoothTransformation)

                        # Создаем QLabel для отображения изображения
                        label = QLabel()
                        label.setPixmap(pixmap)
                        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # PyQt6

                        # Устанавливаем QLabel в ячейку
                        #self.ui.tableWidget.tableWidget.setCellWidget(ii, jj, label)
                    else:
                        pixmap = QPixmap("Form6.jpg")
                        print(pixmap)
                        pixmap = pixmap.scaled(100, 150,
                                               Qt.AspectRatioMode.KeepAspectRatio,
                                               Qt.TransformationMode.SmoothTransformation)

                        # Создаем QLabel для отображения изображения
                        label = QLabel()
                        label.setPixmap(pixmap)
                        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # PyQt6

                    self.ui.tableWidget.setCellWidget(ii, jj, label)
                jj += 1
        self.ui.tableWidget.resizeRowsToContents()

    def closeEvent(self, event):
        event.accept()  # Разрешаем закрытие
        if self.bool:
            self.parent.bool = True
            self.parent.show()
