'''Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
'''

#Comenzando a declarar variables para el largo y ancho
length = float(input("Ingresa la longitud del cuarto: "))
widht = float(input("Ingresa el ancho del cuarto: "))
area = length*widht
print(f"El área de la habitación es {area}")