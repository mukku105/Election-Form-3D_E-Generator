
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic
from pypdf import PdfWriter
import pandas as pd
import sqlite3


# class ElectionForm3DEGenerator:
#     def generate_form(self):
#         token = self.ui.le_watoken.text().strip()
#         if token:
#             try:
#                 conn = sqlite3.connect('election_form.db')
#                 c = conn.cursor()
#                 c.execute('CREATE TABLE IF NOT EXISTS election_nomination_details (id INTEGER PRIMARY KEY, sl_no INTEGER, name TEXT, guardians_name TEXT, age INTEGER, address TEXT, particulars_of_origin TEXT, party_affiliation TEXT, assembly_con TEXT, part_no TEXT, ser_no TEXT, proposer TEXT, prop_part_no TEXT, prop_serial_no TEXT, nomination_date TEXT)')

#                 c.execute('SELECT * FROM election_form')
#                 conn.commit()
#                 conn.close()
#             except sqlite3.Error as e:
#                 print(e)
#                 QMessageBox.critical(self, 'Error', 'An error occurred while creating the database')
#                 return

try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    pass

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('./ui/main_ui.ui', self)
        self.setFixedSize(512, 540)
        self.setWindowTitle('Election Form 3D_E Generator')

        try:
            with open('config.conf', 'rb') as f:
                encrypted_token = f.read().decode()
                self.ui.le_watoken.setText(encrypted_token)
        except FileNotFoundError:
            pass

        self.show()

    def save_file(self):
        token = self.ui.le_watoken.text().strip()
        if token:
            encrypted_token = self.xor_encrypt_decrypt(token, self.xor_enc_key)
            with open('config.conf', 'wb') as f:
                f.write(encrypted_token.encode())
            QMessageBox.information(self, 'Success', 'Token saved successfully')
        else:
            QMessageBox.critical(self, 'Error', 'Please enter a valid token')  

    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())