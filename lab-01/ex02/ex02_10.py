def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Nhập một chuỗi cần đảo ngược: ")
print("Chuỗi sau khi đảo ngược là:", dao_nguoc_chuoi(input_string))