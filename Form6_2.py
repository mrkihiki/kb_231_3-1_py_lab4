import sqlite3
import base64
import io

from PIL import Image
from datetime import date

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox

from Form6_2_ui import Ui_MainWindow as Form6_2_ui


class Form6_2(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form6_2_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.id = int(self.parent.ui.spinBox.text())
        if not self.parent.bool_new:
            cur = self.parent.parent.connection.cursor()
            temp =  [item for item in cur.execute("SELECT title,author,year,genre FROM books WHERE id = ?",(self.id,)).fetchone()]
            self.ui.lineEdit.setText(temp[0])
            self.ui.lineEdit_2.setText(temp[1])
            self.ui.spinBox.setValue(temp[2])
            self.ui.lineEdit_3.setText(temp[3])
        self.ui.pushButton.clicked.connect(self.run)
        self.ui.pushButton_2.clicked.connect(self.close)

    @staticmethod
    def optimize_image_to_blob(image_path, max_size=(200, 300), max_kb=50):
        # Оптимизирует изображение до указанного размера

        # Args:
        #     image_path: путь к изображению
        #     max_size: максимальные размеры
        #     max_kb: максимальный размер в KB

        # Returns:
        #     bytes: оптимизированные данные
        try:
            with Image.open(image_path) as img:
                # Конвертируем в RGB
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # Масштабируем
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

                # Постепенно уменьшаем качество пока не достигнем нужного размера
                quality = 85
                while quality >= 30:
                    buffer = io.BytesIO()
                    img.save(buffer, format='JPEG', quality=quality, optimize=True)

                    if len(buffer.getvalue()) <= max_kb * 1024 or quality <= 30:
                        print(buffer.getvalue())
                        return base64.b64encode(buffer.getvalue()).decode('utf-8')

                    quality -= 15

                return base64.b64encode(buffer.getvalue()).decode('utf-8')

        except Exception as e:
            print(f"Ошибка оптимизации изображения: {e}")
            return "None"

    def run(self):
        if "" in [" ".join(self.ui.lineEdit.text().split()), " ".join(self.ui.lineEdit_2.text().split()), " ".join(self.ui.lineEdit_3.text().split())]:
            QMessageBox.warning(
                self, '', "Заполните все столбцы",
                QMessageBox.StandardButton.Ok)
            return
        cur = self.parent.parent.connection.cursor()
        if self.parent.bool_new:
            img = self.optimize_image_to_blob(self.ui.lineEdit_4.text())
            params = [
                self.ui.lineEdit.text(),
                self.ui.lineEdit_2.text(),
                int(self.ui.spinBox.value()),
                self.ui.lineEdit_3.text(),
                img
            ]
            params[0] = " ".join(params[0].split())
            que = "INSERT INTO books (title, author, year, genre, image) VALUES(?, ?, ?, ?, ?)"
            cur.execute(que, params)
            self.parent.parent.connection.commit()
            self.parent.select_data()
            self.close()
        else:
            que = "UPDATE films SET\n"
            img = self.optimize_image_to_blob(self.ui.lineEdit_4.text())
            if img is None:
                params = [
                    self.ui.lineEdit.text(),
                    self.ui.lineEdit_2.text(),
                    int(self.ui.spinBox.value()),
                    self.ui.lineEdit_3.text()
                ]
                que += ", ".join([f"{col} = ?" for col in self.parent.names[1:5]])
            else:
                params = [
                    self.ui.lineEdit.text(),
                    self.ui.lineEdit_2.text(),
                    int(self.ui.spinBox.value()),
                    self.ui.lineEdit_3.text(),
                    img
                ]
                que += ", ".join([f"{col} = ?" for col in self.parent.names[1:]])
            params[0] = " ".join(params[0].split())
            que += " WHERE id = ?"
            cur.execute(que, (params + [int(self.id)]))
            self.parent.connection.commit()
            self.parent.select_data()
            self.close()

    def closeEvent(self, event):
        # self.connection.close()
        event.accept()  # Разрешаем закрытие
        self.parent.bool = True
        self.parent.show()
