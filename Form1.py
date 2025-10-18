import csv

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem

from Form1_ui import Ui_MainWindow as Form1_ui


class Form1(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.ui = Form1_ui()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.run('rez.csv')
        self.ui.pushButton.clicked.connect(lambda: self.filtertabl('rez.csv'))

    def run(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            school = []
            clas = []
            score = 9999
            num_score = 0
            title = next(reader)
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels((title[1], title[2], title[7]))
            self.ui.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.ui.tableWidget.setRowCount(
                    self.ui.tableWidget.rowCount() + 1)
                if row[2].split('-')[2] not in school:
                    school.append(row[2].split('-')[2])
                if row[2].split('-')[3] not in clas:
                    clas.append(row[2].split('-')[3])
                for j, elem in enumerate([row[1], row[2], row[7]]):
                    self.ui.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
                if num_score < 4:
                    if score > int(row[7]):
                        num_score += 1
                        score = int(row[7])
                    if num_score != 4:
                        for j in range(self.ui.tableWidget.columnCount()):
                            self.ui.tableWidget.item(i, j).setBackground(QColor('red'))
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.comboBox.addItems(sorted(clas))
        self.ui.comboBox_2.addItems(sorted(school))

    def filtertabl(self, table_name):
        clas = self.ui.comboBox.currentText()
        school = self.ui.comboBox_2.currentText()
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=',', quotechar='"')
            title = next(reader)
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels((title[1], title[2], title[7]))
            self.ui.tableWidget.setRowCount(0)
            i = 0
            score = 9999
            num_score = 0
            for row in reader:
                if school != '':
                    if row[2].split('-')[2] not in school:
                        continue
                if clas != '':
                    if row[2].split('-')[3] not in clas:
                        continue
                self.ui.tableWidget.setRowCount(
                    self.ui.tableWidget.rowCount() + 1)
                for j, elem in enumerate([row[1], row[2], row[7]]):
                    self.ui.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
                if num_score < 4:
                    if score > int(row[7]):
                        num_score += 1
                        score = int(row[7])
                    if num_score != 4:
                        for j in range(self.ui.tableWidget.columnCount()):
                            self.ui.tableWidget.item(i, j).setBackground(QColor('red'))
                i += 1

        self.ui.tableWidget.resizeColumnsToContents()

    def closeEvent(self, event):
        event.accept()  # Разрешаем закрытие
        self.parent.show()
