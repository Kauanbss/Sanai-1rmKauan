def maior(n1, n2, n3):
    if (n1 > n2 and n1 > n3):
        return n1
    elif (n2 > n1 and n2 > n3):
        return n2
    alse:
        return n3
     

 a =int(input("numeros 1: "))
 b =int(input("numeros 2: "))
 c =int(input("numeros 3: "))

 print(maior(a, b, c))
