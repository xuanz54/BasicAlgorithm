def CaeserDecode(cipherText, key):
    """
    使用凯撒解密算法对输入的密文进行解密。

    :param cipherText: str, 需要解密的密文
    :param key: int, 用于解密的密钥
    :return: str, 解密后的明文
    """
    decrypted_text = []  # 存储解密后的字符
    for char in cipherText:
        if 'A' <= char <= 'Z':
            # 计算解密后的字符，利用ASCII码的偏移量和循环位移
            decrypted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        elif 'a' <= char <= 'z':
            # 计算解密后的字符，利用ASCII码的偏移量和循环位移
            decrypted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)
        else:
            # 非字母字符直接添加到结果中，不进行解密
            decrypted_text.append(char)

    # 将字符列表合并为字符串并返回
    return ''.join(decrypted_text)

def brute_force_caesar(cipherText):
    """
    使用暴力破解方法尝试所有可能的密钥来解密凯撒密码密文。

    :param cipherText: str, 需要解密的密文
    :return: None, 直接打印所有可能的解密结果
    """
    for key in range(26):  # 尝试所有可能的密钥
        decrypted_text = CaeserDecode(cipherText, key)
        print(f"密钥 {key}: {decrypted_text}")


# 示例密文
cipherText = "bafalsaewa"
# 尝试暴力破解解密密文
brute_force_caesar(cipherText)
