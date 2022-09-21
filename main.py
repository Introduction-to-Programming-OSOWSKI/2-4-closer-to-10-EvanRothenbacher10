def close10(x, y):
    if x - 10 > y - 10:
        return x
    elif y - 10 > x - 10:
        return y
    else:
        return 0

print(close10(5, 13))