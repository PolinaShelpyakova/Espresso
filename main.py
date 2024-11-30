import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPlainTextEdit
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
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
