"""
Con complejidad O(n)

def conv_str_digi(stri, lon):
    
    if lon == 0:
        return int(stri[lon])

    return conv_str_digi(stri, lon-1)*10 + int(stri[lon])"""

def conv_str_digi(stri, start, end):

    if start == end:
        return int(stri[start])

    mid = (start + end) // 2
    left_part = conv_str_digi(stri, start, mid)
    right_part = conv_str_digi(stri, mid + 1, end)

    factor = 10 ** (end - mid)

    return left_part * factor + right_part
    
stri = '123'

nume = conv_str_digi(stri, 0, len(stri)-1)

print(nume)