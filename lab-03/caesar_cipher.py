import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# Khớp nối chuẩn với giao diện trong thư mục ui
from ui.caesar import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối chính xác với tên nút bấm pushButton và pushButton_2 từ file ui
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        # Đã đồng bộ sang cổng 5050 theo đúng Server Flask thực tế của bro
        url = "http://127.0.0.1:5050/api/caesar/encrypt"
        
        plaintext = self.ui.txtInputText.toPlainText()
        key = self.ui.txtKey.text()
        
        payload = {
            "plain_text": plaintext,
            "key": key
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị chuỗi đã mã hóa nhận từ Server lên ô Kết quả
                self.ui.txtResult.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        # Đã đồng bộ sang cổng 5050 theo đúng Server Flask thực tế của bro
        url = "http://127.0.0.1:5050/api/caesar/decrypt"
        
        # Khi giải mã, lấy text từ ô txtInputText gửi lên server
        ciphertext = self.ui.txtInputText.toPlainText()
        key = self.ui.txtKey.text()
        
        payload = {
            "cipher_text": ciphertext,
            "key": key
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị chuỗi đã giải mã nhận từ Server lên ô Kết quả
                self.ui.txtResult.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())