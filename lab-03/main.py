import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.caesar import Ui_MainWindow

# Thuật toán mã hóa Caesar tự viết
class CaesarCipher:
    def encrypt(self, text, key):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
        return result

    def decrypt(self, text, key):
        return self.encrypt(text, -key)


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ĐÃ SỬA: Kết nối đúng với pushButton và pushButton_2 của Qt Designer mặc định
        self.ui.pushButton.clicked.connect(self.xu_ly_ma_hoa)
        self.ui.pushButton_2.clicked.connect(self.xu_ly_giai_ma)

    def xu_ly_ma_hoa(self):
        try:
            plaintext = self.ui.txtInputText.toPlainText()
            key = int(self.ui.txtKey.text())
            
            cipher = CaesarCipher()
            ket_qua = cipher.encrypt(plaintext, key)
            
            self.ui.txtResult.setPlainText(ket_qua)
        except Exception as e:
            self.ui.txtResult.setPlainText(f"Lỗi nhập liệu rồi bro: {str(e)}")

    def xu_ly_giai_ma(self):
        try:
            ciphertext = self.ui.txtInputText.toPlainText()
            key = int(self.ui.txtKey.text())
            
            cipher = CaesarCipher()
            ket_qua = cipher.decrypt(ciphertext, key)
            
            self.ui.txtResult.setPlainText(ket_qua)
        except Exception as e:
            self.ui.txtResult.setPlainText(f"Lỗi nhập liệu rồi bro: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())