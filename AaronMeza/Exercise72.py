line = input("Ingresa una linea: ")
es_palindromo = True

for i in range(0, len(line)//2):
    if line[i] != line[len(line) - i - 1]:
        es_palindromo = False


if es_palindromo:
    print(line, " es un palindromo")
else:
    print(line, "no es un palindromo")