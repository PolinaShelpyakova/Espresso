import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QPlainTextEdit
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 448)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 831, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 231, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 330, 231, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить/Изменить запись о кофе"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить таблицу"))


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 45, 371, 41))
        self.label_2.setObjectName("label_2")
        self.roasting = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.roasting.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.roasting.setObjectName("roasting")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 100, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 150, 161, 16))
        self.label_4.setObjectName("label_4")
        self.status = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.status.setObjectName("status")
        self.description = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.description.setGeometry(QtCore.QRect(10, 190, 191, 31))
        self.description.setObjectName("description")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 200, 161, 16))
        self.label_5.setObjectName("label_5")
        self.price = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(10, 240, 191, 31))
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 250, 161, 16))
        self.label_6.setObjectName("label_6")
        self.volume = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(10, 290, 191, 31))
        self.volume.setObjectName("volume")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 300, 181, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 121, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите сорт кофе"))
        self.label_2.setText(_translate("MainWindow", "........................................................."
                                                      ".................................."))
        self.label_3.setText(_translate("MainWindow", "Введите степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "Кофе молотый или в зёрнах?"))
        self.label_5.setText(_translate("MainWindow", "Опишите вкус кофе"))
        self.label_6.setText(_translate("MainWindow", "Укажите цену"))
        self.label_7.setText(_translate("MainWindow", "Укажите объём кофе в упоковке"))
        self.pushButton.setText(_translate("MainWindow", "Подтвердить"))


class SecondWindow(QMainWindow, Ui_MainWindow_2):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


class Coffee(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("release/data/coffee.sqlite")
        self.update_table()
        self.w = SecondWindow(self)
        self.pushButton.clicked.connect(self.second_window)
        self.pushButton_2.clicked.connect(self.update_table)
        self.buttons_from_w = [self.w.label_3, self.w.label_4, self.w.label_5, self.w.label_6, self.w.label_7,
                               self.w.roasting, self.w.status, self.w.description, self.w.price, self.w.volume]
        self.coffee_name = None

    def update_table(self):
        res = self.connection.cursor().execute("""SELECT id, name, roasting, status, description, price, volume
                FROM CoffeeSort""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.resizeColumnsToContents()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def second_window(self):
        self.w.show()
        for i in self.buttons_from_w:
            i.hide()
        self.w.pushButton.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        if self.coffee_name != self.w.name.toPlainText():
            self.coffee_name = self.w.name.toPlainText()
            if (self.w.name.toPlainText(),) in self.connection.cursor().execute("""SELECT name 
            FROM CoffeeSort""").fetchall():
                self.info_coffee = self.connection.cursor().execute(f"""SELECT * FROM CoffeeSort 
                WHERE name like '{self.w.name.toPlainText()}'""").fetchall()[0]
            else:
                self.info_coffee = None
            if self.info_coffee is None:
                self.w.label_2.setText('В БД ещё нет такого сорта кофе,\nдобавьте информацию об этом сорте')
            else:
                self.w.label_2.setText('В БД есть такой сорт кофе,\nВы можете изменить информацию об этом сорте')
            for i in self.buttons_from_w:
                i.show()
        else:
            if all(i.toPlainText() != '' for i in self.buttons_from_w if type(i) == QPlainTextEdit):
                if self.info_coffee is None:
                    self.connection.cursor().execute(f"""INSERT INTO CoffeeSort(name,roasting,status,description,price,
                    volume) VALUES('{self.coffee_name}','{self.w.roasting.toPlainText()}',
                    '{self.w.status.toPlainText()}','{self.w.description.toPlainText()}',
                    '{self.w.price.toPlainText()}','{self.w.volume.toPlainText()}')""")
                else:
                    self.connection.cursor().execute(f"""UPDATE CoffeeSort
                    SET roasting = '{self.w.roasting.toPlainText()}', 
                    status = '{self.w.roasting.toPlainText()}', 
                    description = '{self.w.description.toPlainText()}', 
                    price = '{self.w.price.toPlainText()}', 
                    volume = '{self.w.volume.toPlainText()}'
                    WHERE name = '{self.coffee_name}'""")
                self.w.label_2.setText('Информация заполнена!')
                self.coffee_name = None
                for i in self.buttons_from_w:
                    if type(i) == QPlainTextEdit:
                        i.setPlainText('')
                    i.hide()
                self.w.name.setPlainText('')
                self.connection.commit()
            else:
                self.w.label_2.setText(f'Вы не заполнили информацию о сорте {self.coffee_name}!!!')

    def closeEvent(self, event):
        self.connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Coffee()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
