def decimal_to_base62(decimal_num):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base62_num = ""

    while decimal_num > 0:
        remainder = decimal_num % 66
        base62_num = characters[remainder] + base62_num
        decimal_num //= 66

    return base62_num if base62_num else "0"