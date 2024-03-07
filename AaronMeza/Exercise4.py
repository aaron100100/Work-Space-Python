'''  
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
'''
#Medidas ingresadas por el usuario
length = int(input("Ingresa la longitud del campo en pies: "))
width = int(input("Ingresa el ancho del campo en pies: "))
#Cálculo del área
area = length*width
# Aqui viene la conversión
area = area / 43560

print(f'El área del campo en acres es de {area}')