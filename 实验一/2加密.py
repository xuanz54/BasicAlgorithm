def CaeserEncode(plainText, key):
    """
    使用凯撒加密算法对输入的明文进行加密。

    :param plainText: str, 需要加密的明文
    :param key: int, 用于加密的密钥
    :return: str, 加密后的密文
    """
    encrypted_text = []  # 存储加密后的字符
    for char in plainText:
        if 'A' <= char <= 'Z':
            # 计算加密后的字符，利用ASCII码的偏移量和循环位移
            encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        elif 'a' <= char <= 'z':
            # 计算加密后的字符，利用ASCII码的偏移量和循环位移
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)
        else:
            # 非字母字符直接添加到结果中，不进行加密
            encrypted_text.append(char)

    # 将字符列表合并为字符串并返回
    return ''.join(encrypted_text)

# 示例运行
plainText = "I Love YNUFE!"  # 要加密的明文
key = 3                    # 用于加密的密钥
# 调用凯撒加密函数进行加密
cipherText = CaeserEncode(plainText, key)
# 打印加密结果
print(f"明文：{plainText}")
print(f"密钥：{key}")
print(f"密文：{cipherText}")
