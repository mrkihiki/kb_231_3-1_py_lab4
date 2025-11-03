import os
import sqlite3
import sys
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from Form6_ui import Ui_MainWindow as MainFormUI
from Form6_1 import Form6_1
import hashlib
import base64

def resource_path(relative_path):
    """Получает правильный путь к ресурсам для dev и exe"""
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Form6(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        # uic.loadUi('start_ui.py', self)  # Загружаем дизайн
        self.ui = MainFormUI()
        self.ui.setupUi(self)
        self.parent = args[-1]
        self.bool = True
        self.connection = sqlite3.connect(resource_path(os.path.join('', 'Form6.db')))
        self.ui.pushButton.clicked.connect(lambda: self.open_form(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.open_form(2))

    @staticmethod
    def hash_password_with_salt(password, salt=None):
        if salt is None:
            salt = os.urandom(32)  # Генерируем случайную соль

        # Комбинируем пароль и соль
        password_salt = password.encode() + salt
        hashed = hashlib.sha256(password_salt).hexdigest()
        salt = base64.b64encode(salt).decode('utf-8')

        return hashed, salt

    @staticmethod
    def verify_password_with_salt(password, hashed, salt):
        #Проверка пароля
        salt = base64.b64decode(salt.encode('utf-8'))
        test_hash, _ = Form6.hash_password_with_salt(password, salt)

        return test_hash == hashed

    def open_form(self, form_number):
        cursor = self.connection.cursor()
        login = self.ui.lineEdit.text()
        if login is None or login == "":
            self.ui.label_3.setText("Введите логин")
            return
        if form_number == 1:
            if cursor.execute("SELECT 1 FROM users WHERE login = ?", (login,)).fetchone():
                if (self.verify_password_with_salt(self.ui.lineEdit_2.text(), *cursor.execute("SELECT pass, salt FROM users WHERE login = ?",
                                                                                             login).fetchone())):
                    # self.loggin_id = cursor.execute("SELECT id FROM users WHERE login = ? and password = ?",
                    #                                 (login, self.ui.lineEdit_2.text())).fetchone()[0]
                    self.form = Form6_1(self)
                    self.bool = False
                    self.form.show()
                    self.close()
                else:
                    self.ui.label_3.setText("Неправильный пароль")
            else:
                self.ui.label_3.setText("Пользователь не найден")
        elif form_number == 2:
            if cursor.execute("SELECT 1 FROM users WHERE login = ?", (login,)).fetchone() is None:
                if self.ui.lineEdit_2.text() is (None or ""):
                    self.ui.label_3.setText("Введите пароль")
                else:
                    cursor.execute(
                        "INSERT INTO users (login, pass, salt) VALUES (?, ?, ?)",
                        (login,*self.hash_password_with_salt(self.ui.lineEdit_2.text()))
                    )
                    self.connection.commit()
                    self.ui.label_3.setText("Зарегистрирован")
            else:
                self.ui.label_3.setText("Ошибка: Логин уже существует")

    def closeEvent(self, event):
        if self.bool:
            self.parent.show()
        event.accept()