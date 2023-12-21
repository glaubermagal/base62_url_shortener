def decimal_to_base66(decimal_num):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.~"
    base66_num = ""

    while decimal_num > 0:
        remainder = decimal_num % 66
        base66_num = characters[remainder] + base66_num
        decimal_num //= 66

    return base66_num if base66_num else "0"