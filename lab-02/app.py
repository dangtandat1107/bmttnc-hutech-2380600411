import sys
import os

# Ép Python tìm kiếm module bên trong thư mục ex01 để tránh lỗi ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ex01')))

from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher  # ĐÃ FIX: Chữ F viết hoa chuẩn lớp gốc

app = Flask(__name__)

# ==================== HOME ROUTE ====================
@app.route("/")
def home():
    return render_template('index.html')


# ==================== CAESAR CIPHER ====================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==================== VIGENERE CIPHER ====================
@app.route("/vigenere")
def vigenere_page():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==================== RAIL FENCE CIPHER ====================
@app.route("/railfence")
def railfence_page():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key) 
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key) 
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==================== PLAYFAIR CIPHER ====================
# ĐÃ BỔ SUNG: Route hiển thị giao diện Playfair để không bị lỗi 404
@app.route("/playfair")
def playfair_page():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    
    # Tạo ma trận từ Key trước khi thực hiện mã hóa theo đúng logic Playfair
    playfair_matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, playfair_matrix) 
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    
    # Tạo ma trận từ Key trước khi thực hiện giải mã
    playfair_matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, playfair_matrix) 
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==================== MAIN RUNNER ====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)