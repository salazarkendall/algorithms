def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mueve el disco 1 desde {origen} hasta {destino}")
        return
    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mueve el disco {n} desde {origen} hasta {destino}")
    torres_de_hanoi(n - 1, auxiliar, destino, origen)


# Número de discos
n = 3
# Llamada a la función con la cantidad de discos y nombres de las varillas
torres_de_hanoi(n, 'A', 'C', 'B')
