#Complejidad O(n)

def conv_str_digi(stri, lon):
    
    if lon == 0:
        return int(stri[lon])
    
    return conv_str_digi(stri, lon-1)*10 + int(stri[lon])

stri = "123"

print(conv_str_digi(stri, len(stri)-1))
print(type(conv_str_digi(stri, len(stri)-1)))