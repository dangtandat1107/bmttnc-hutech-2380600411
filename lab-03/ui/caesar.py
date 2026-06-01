import os
import sys
# Ép cấu hình nền tảng platforms theo tài liệu của thầy
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Tiêu đề app
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 40, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("CAESAR CIPHER.")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Tên sinh viên
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 90, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("Dang Tan Dat - 2380600411")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        
        # Nhãn Plain Text
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 100, 30))
        self.label_3.setText("Plain Text:")
        
        # Ô nhập Plain Text
        self.txtInputText = QtWidgets.QTextEdit(self.centralwidget)
        self.txtInputText.setGeometry(QtCore.QRect(160, 150, 500, 80))
        
        # Nhãn Key
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 100, 30))
        self.label_4.setText("Key:")
        
        # Ô nhập Key
        self.txtKey = QtWidgets.QLineEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(160, 260, 500, 30))
        
        # Nhãn Cipher Text
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 100, 30))
        self.label_5.setText("Cipher Text:")
        
        # Ô hiển thị kết quả
        self.txtResult = QtWidgets.QTextEdit(self.centralwidget)
        self.txtResult.setGeometry(QtCore.QRect(160, 320, 500, 120))
        
        # Nút Mã hóa (Encrypt)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 480, 100, 40))
        self.pushButton.setText("Encrypt")
        
        # Nút Giải mã (Decrypt)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 480, 100, 40))
        self.pushButton_2.setText("Decrypt")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Kết nối nút bấm với hàm xử lý logic thuật toán
        self.pushButton.clicked.connect(self.xu_ly_ma_hoa)
        self.pushButton_2.clicked.connect(self.xu_ly_giai_ma)

    # Thuật toán xử lý mã hóa Caesar
    def caesar_cipher(self, text, key):
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
        return result

    def xu_ly_ma_hoa(self):
        try:
            plaintext = self.txtInputText.toPlainText()
            key = int(self.txtKey.text())
            ket_qua = self.caesar_cipher(plaintext, key)
            self.txtResult.setPlainText(ket_qua)
        except Exception as e:
            self.txtResult.setPlainText(f"Lỗi nhập liệu: {str(e)}")

    def xu_ly_giai_ma(self):
        try:
            ciphertext = self.txtInputText.toPlainText()
            key = int(self.txtKey.text())
            ket_qua = self.caesar_cipher(ciphertext, -key)
            self.txtResult.setPlainText(ket_qua)
        except Exception as e:
            self.txtResult.setPlainText(f"Lỗi nhập liệu: {str(e)}")

# Khởi chạy ứng dụng trực tiếp từ file này luôn theo chuẩn slide thầy
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())