def cuenta_ahorro(anios, dinero):
    interes = 0.04
    for _ in range(anios):
        dinero = dinero + dinero*interes
    return dinero

dinero = float(input("Ingresa el dinero: "))
anios = int(input("Ingresa el número de años: "))

print(f'Tus ahorros son {cuenta_ahorro(anios, dinero)}')
