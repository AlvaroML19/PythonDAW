#Escribe mayor(a, b) que devuelva el mayor de dos números, sin usar max().

def mayor (a:float, b:float):
    return a if a > b else b 

print (mayor(4, 9))
print (mayor(9, 4))