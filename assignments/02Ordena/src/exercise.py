def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if (x >= y) and (x >= z) and (z >= y):
        print(y)
        print(z)
        print(x)
    elif (z >= x) and (z >= y) and (x >= y):
        print(y)
        print(x)
        print(z)
    elif (x >= y) and (x >= z) and (y >= z):
        print(z)
        print(y)
        print(x)
    elif (y >= x) and (y >= z) and (x >= z):
        print(z)
        print(x)
        print(y)
    elif (y >= x) and (y >= z) and (z >= x):
        print(x)
        print(z)
        print(y)
    elif (z >= x) and (z >= y) and (y >= x):
        print(x)
        print(y)
        print(z)

if __name__=='__main__':
    main()
