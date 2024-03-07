''' In many jurisdictions a small deposit is added to drink containers to encourage peopleto recycle them. 
In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, 
and drink containers holding more than one liter have a $0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will bereceived 
for returning those containers. 
Format the output so that it includes a dollar sign and always displays exactly two decimal places   '''

contenedores_tipo_1 = int(input("¿Cuántos contenedores con capacidad de un litro o menos tiene usted?"))
contenedores_tipo_2 = int(input("¿Cuántos contenedores con capacidad de más de un litro tiene usted?"))

print("El rembolso para los contenedores de capacidad de un litro o menos es: {:.2f}".format(contenedores_tipo_1*.10))
print("El remobolso para los contenedores de capacidad más de un litro es: {:.2f}".format(contenedores_tipo_2*.25))