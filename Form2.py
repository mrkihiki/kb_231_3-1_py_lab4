import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox

from Form2_ui import Ui_MainWindow as Form2_ui
from Form2_1 import Form2_1


class Form2(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form2_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.connection = sqlite3.connect("films_db.sqlite")
        self.bool = False
        self.bool_new = True
        self.genre = dict(self.connection.cursor().execute("SELECT * FROM genres").fetchall())
        self.ui.pushButton.clicked.connect(self.delete_elem)
        # self.pushButton.clicked.connect(self.select_data)
        # По умолчанию будем выводить все данные из таблицы films
        self.select_data()
        self.form = Form2_1(self)
        self.ui.pushButton_2.clicked.connect(
            lambda: (
                self.form.close(),
                setattr(self, 'bool_new', False), setattr(self, 'form', Form2_1(self)), self.form.show(),
                setattr(self, 'bool', True)) if int(self.ui.spinBox.text()) in [item[0] for item in
                                                                                self.res] else QMessageBox.warning(
                self, '', f"Нету записи с id = {self.ui.spinBox.text()}",
                QMessageBox.StandardButton.Ok))
        self.ui.pushButton_3.clicked.connect(
            lambda: (
                self.form.close(),
                setattr(self, 'bool_new', True), setattr(self, 'form', Form2_1(self)), self.form.show(),
                setattr(self, 'bool', True)))

    def select_data(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        query = "SELECT * FROM films"
        self.res = self.connection.cursor().execute(query).fetchall()
        self.names = [item[0] for item in
                      self.connection.cursor().execute("SELECT name FROM pragma_table_info('films')").fetchall()]
        # Заполним размеры таблицы
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.names)
        # Заполняем таблицу элементами
        for i, row in enumerate(self.res):
            self.ui.tableWidget.setRowCount(
                self.ui.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if j != 3:
                    self.ui.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
                else:
                    self.ui.tableWidget.setItem(
                        i, j, QTableWidgetItem(self.genre[elem]))

    def delete_elem(self):
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
            cur = self.connection.cursor()
            cur.execute("DELETE FROM films WHERE id = ?", (id,))
            self.connection.commit()
            self.select_data()

    def closeEvent(self, event):
        if self.bool:
            self.form.close()
        self.connection.close()
        event.accept()  # Разрешаем закрытие
        self.parent.show()
