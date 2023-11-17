import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUi()

    def initUi(self):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'название сорт', 'степень обжарки', 'молотый/в зернах',
                                              'описание вкуса', 'цена', 'объем упаковки'])
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        res = self.cur.execute('SELECT * FROM coffee_info').fetchall()
        self.table.setRowCount(len(res))
        print(res)
        for i, info in enumerate(res):
            self.table.setItem(i, 0, QTableWidgetItem(str(info[0])))
            self.table.setItem(i, 1, QTableWidgetItem(str(info[1])))
            self.table.setItem(i, 2, QTableWidgetItem(str(info[2])))
            self.table.setItem(i, 3, QTableWidgetItem(str(info[3])))
            self.table.setItem(i, 4, QTableWidgetItem(str(info[4])))
            self.table.setItem(i, 5, QTableWidgetItem(str(info[5])))
            self.table.setItem(i, 6, QTableWidgetItem(str(info[6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
