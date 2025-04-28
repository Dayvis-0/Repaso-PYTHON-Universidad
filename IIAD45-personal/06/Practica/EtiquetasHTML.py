def eti_html(text):
    stack = []
    j = text.find("<")

    while j != -1:
        k = text.find(">", j+1) 

        if k == -1:
            return False
        
        eti = text[j+1:k]

        if not eti.startswith("/"):
            stack.append(eti)
        else:
            if len(stack) == 0:
                return False
            if eti[1:] != stack.pop():
                return False
            
        j = text.find("<", k+1)
        
    return len(stack) == 0

if eti_html("<h1></h1>"):
    print("Si")
else:
    print("no")