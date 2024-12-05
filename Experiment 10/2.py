def validPalindrome(s):
    """
    判断给定的字符串是否可以通过删除最多一个字符变成回文串。
    :param s: 非空字符串
    :return: 布尔值，表示是否可以变成回文串
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 检查删除左边或右边的字符后是否形成回文
            return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
        left += 1
        right -= 1
    return True
def print_result(res):
    if res:
        print("可以通过删除一个字符变成回文串或者本身就是回文串。")
    else:
        print("删除任何一个字符都不能使之变成回文串。")
# 测试用例
print("请输入字符串:aba")
print_result(validPalindrome("aba"))  
print("请输入字符串:abca")
print_result(validPalindrome("abca"))  
print("请输入字符串:abc")
print_result(validPalindrome("abc"))  