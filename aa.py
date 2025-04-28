nume = 123
resu = 0
mult = 10

while nume != 0:
    divi = nume % 10
    resu = (resu)*mult + divi
    nume //= 10

print(resu)
"""nume = 123
print(nume % 10)
print(nume // 10)"""