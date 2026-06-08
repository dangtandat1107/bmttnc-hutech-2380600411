import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    # Trích xuất tất cả các bit cuối cùng từ các pixel ảnh
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Phân tách chuỗi bit thành các ký tự văn bản (mỗi cụm 8 bit)
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        # Nếu gặp ký tự kết thúc ký hiệu bởi chuỗi bit kết thúc ngắt, dừng lại
        if binary_message[i:i+16] == '1111111111111110' or char == '\x00':
            break
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
        
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()