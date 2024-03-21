
import itertools
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic
from pypdf import PdfWriter

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