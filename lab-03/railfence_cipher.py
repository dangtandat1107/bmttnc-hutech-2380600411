import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow

class RailFenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5050/api/railfence/encrypt"
        try:
            payload = {
                "plain_text": self.ui.txtInputText.toPlainText(),
                "key": int(self.ui.txtKey.text())
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtResult.setText(data.get("encrypted_message", ""))
                QMessageBox.information(self, "Success", "Encrypted Successfully!")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Key must be an integer number!")
        except Exception as e:
            QMessageBox.critical(self, "Exception", f"Connect failed: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5050/api/railfence/decrypt"
        try:
            payload = {
                "cipher_text": self.ui.txtResult.toPlainText(),
                "key": int(self.ui.txtKey.text())
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # SỬA TẠI ĐÂY: Đổi sang txtResult để kết quả đổ xuống ô bên dưới
                self.ui.txtResult.setText(data.get("decrypted_message", ""))
                QMessageBox.information(self, "Success", "Decrypted Successfully!")
            else:
                QMessageBox.warning(self, "Error", "Error while calling API")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Key must be an integer number!")
        except Exception as e:
            QMessageBox.critical(self, "Exception", f"Connect failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())