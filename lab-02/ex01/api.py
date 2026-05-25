import sys
import os
from flask import Flask, request, jsonify

# Thiết lập đường dẫn tìm kiếm module để tránh lỗi ModuleNotFoundError
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Khởi tạo các đối tượng Cipher một lần ở đầu hệ thống
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()


# ==================== CAESAR CIPHER ====================
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


# =================== VIGENERE CIPHER ===================
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(text, key)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(text, key)})


# =================== RAILFENCE CIPHER ===================
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = int(data['key'])
    return jsonify({'encrypted_text': railfence_cipher.rail_fence_encrypt(text, key)})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = int(data['key'])
    return jsonify({'decrypted_text': railfence_cipher.rail_fence_decrypt(text, key)})


# ==================== PLAYFAIR CIPHER ====================
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(text, playfair_matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(text, playfair_matrix)})


# ==================== MAIN RUNNER ====================
# Luôn đặt khối lệnh app.run ở dưới cùng của file api.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)