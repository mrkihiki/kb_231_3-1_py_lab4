import sqlite3
from datetime import date

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox

from Form2_1_ui import Ui_MainWindow as Form2_1_ui


class Form2_1(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form2_1_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.id = int(self.parent.ui.spinBox.text())
        self.ui.spinBox.setMaximum(date.today().year)
        first_elements = [item[0] for item in self.parent.res]
        self.ui.comboBox.addItems(list(self.parent.genre.values()))
        if not self.parent.bool_new:
            self.ui.lineEdit.setText(self.parent.res[first_elements.index(int(self.parent.ui.spinBox.text()))][1])
            self.ui.spinBox.setValue(self.parent.res[first_elements.index(int(self.parent.ui.spinBox.text()))][2])
            self.ui.spinBox_2.setValue(self.parent.res[first_elements.index(int(self.parent.ui.spinBox.text()))][4])
            self.ui.comboBox.setCurrentText(
                self.parent.genre.get(self.parent.res[first_elements.index(int(self.parent.ui.spinBox.text()))][3]))
        self.ui.pushButton.clicked.connect(self.run)
        self.ui.pushButton_2.clicked.connect(self.close)

    def run(self):
        params = [
            self.ui.lineEdit.text(),
            int(self.ui.spinBox.text()),
            int(next((k for k, v in self.parent.genre.items() if v == self.ui.comboBox.currentText()), None)),
            int(self.ui.spinBox_2.text())
        ]
        params[0] = " ".join(params[0].split())
        print(params)
        if "" in params:
            QMessageBox.warning(
                self, '', "Заполните все столбцы",
                QMessageBox.StandardButton.Ok)
            return
        cur = self.parent.connection.cursor()
        if self.parent.bool_new:
            que = "INSERT INTO films ("
            que += ", ".join([f"{col}" for col in self.parent.names[1:]])
            que += ") VALUES ("
            que += ", ".join(["? " for col in self.parent.names[1:]])
            que += ")"
            cur.execute(que, params)
            self.parent.connection.commit()
            self.parent.select_data()
            self.close()
        else:
            que = "UPDATE films SET\n"
            que += ", ".join([f"{col} = ?" for col in self.parent.names[1:]])
            que += " WHERE id = ?"
            print(que)
            cur.execute(que, (params + [int(self.id)]))
            self.parent.connection.commit()
            self.parent.select_data()
            self.close()

    def closeEvent(self, event):
        # self.connection.close()
        self.parent.bool = False
        event.accept()  # Разрешаем закрытие
        self.parent.show()
