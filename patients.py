from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem

import sys
from library import Person, Grup  # Import Person and Grup from library.py

app = QtWidgets.QApplication([])
win = uic.loadUi("пациенты.ui")

Gr = Grup()  # Create a Grup object
Gr.read_data_from_file("text.txt")  # Read data from the file
print("!!!", Gr.count)  # You may want to remove this print statement later
win.tableWidget.setRowCount(Gr.count)  # Set the table row count

def btnLoadTable():
    row = 0
    for x in Gr.A:
        win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam + ' ' + Gr.A[x].name + ' ' + Gr.A[x].otchestvo))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].year))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].diagnosis))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(Gr.A[x].hospital_days)))  # Convert hospital_days to a string
        row += 1

win.pushButton.clicked.connect(btnLoadTable)  # Connect the button to the function
win.show()
sys.exit(app.exec_())