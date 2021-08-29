import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    pass

    import math
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    discriminante = (b**2) - (4 * a *c)
    if (a == 0) and (b == 0):
        print("No tiene solucion")
    elif (a == 0) and (b != 0):
        x = (-c) / b
        print(x)
    elif (a != 0) and (b != 0):
        if (discriminante == 0):
            x1 = (-b)/(2*a)
            print(x1)
        elif (discriminante > 0):
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            x3 = (-b + math.sqrt(discriminante))/ (2*a)
            print(x2)
            print(x3)
        else: print("Raices complejas")

if __name__ == '__main__':
    main()
