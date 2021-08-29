def main():
    # Escribe tu código abajo de esta línea
    pass

    grados = int(input("Introduce los grados: "))
    if (grados > 360) or (grados < 0):
        print("excede")
    elif (grados % 90) == 0:
        print("eje")
    elif (90 > grados > 0):
        print("cuadrante 1")
    elif (180 > grados > 90):
        print("cuadrante 2")
    elif (270 > grados > 90):
        print("cuadrante 3")
    elif (360 > grados > 270):
        print("cuadrante 4")

if __name__ == '__main__':
    main()
