def caesar_cipher(text, shift, direction):
    result = ""
    if direction == 'encrypt':
        shift = shift
    else:
        shift = -shift
    for i in text:
        if i.isalpha():  # 如果是字母
            start = ord('A') if i.isupper() else ord('a')
            # 加密或解密
            result += chr(start + (ord(i) - start + shift) % 26)
        else:
            # 非字母字符不变
            result += i
    return result


# 加密
def encrypt(text, shift=3):
    return caesar_cipher(text, shift, 'encrypt')
#这里是定义了一个新的函数来实现对原来的函数的调用，上面的'encrypt'是表示原来
# 来定义的函数所接收的direction的值


# 解密
def decrypt(text, shift=3):
    return caesar_cipher(text, shift, 'decrypt')


while True:
    # 用户输入明文
    plaintext = input("请输入明文（输入'exit'退出）: ")
    if plaintext.lower() == 'exit':
        break
    # 加密
    ciphertext = encrypt(plaintext)
    print(f"明文: {plaintext} -> 密文: {ciphertext}")

    # 询问是否解密
    decrypt_choice = input("是否要解密？(yes/no): ")
    if decrypt_choice.lower() == 'yes':
        # 解密
        decrypted_text = decrypt(ciphertext)
        print(f"密文: {ciphertext} -> 明文: {decrypted_text}")
    else:
        print("好的，我们不解密。")