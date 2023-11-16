def isPalindrome(x: int):
    str_x = str(x)
    reverse = ""
    for i in range(len(str_x)):
        if str_x[i] != str_x[-i-1]:
            return False
        reverse += str_x[-i-1]
    if str_x == reverse:
        return True
print(ispalindrome(22))
