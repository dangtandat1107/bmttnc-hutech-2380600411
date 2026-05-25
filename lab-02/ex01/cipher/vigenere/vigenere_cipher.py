class VigenereCipher:
    def __init__(self):
        # Tự định nghĩa trực tiếp bảng chữ cái tiếng Anh viết hoa chuẩn
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encrypt_text(self, plain_text: str, key: str) -> str:
        alphabet_len = len(self.alphabet)
        plain_text = plain_text.upper()
        key = key.upper()
        encrypted_text = []
        key_index = 0
        
        for letter in plain_text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                key_letter = key[key_index % len(key)]
                key_letter_index = self.alphabet.index(key_letter)
                
                output_index = (letter_index + key_letter_index) % alphabet_len
                encrypted_text.append(self.alphabet[output_index])
                key_index += 1
            else:
                encrypted_text.append(letter)
                
        return "".join(encrypted_text)

    def decrypt_text(self, encrypted_text: str, key: str) -> str:
        alphabet_len = len(self.alphabet)
        encrypted_text = encrypted_text.upper()
        key = key.upper()
        decrypted_text = []
        key_index = 0
        
        for letter in encrypted_text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                key_letter = key[key_index % len(key)]
                key_letter_index = self.alphabet.index(key_letter)
                
                output_index = (letter_index - key_letter_index) % alphabet_len
                decrypted_text.append(self.alphabet[output_index])
                key_index += 1
            else:
                decrypted_text.append(letter)
                
        return "".join(decrypted_text)