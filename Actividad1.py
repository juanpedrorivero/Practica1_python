
#Ejercicio 1;
año = int(input("Ingrese su año de nacimiento: "))
print("Cumplira 18 años en: ",año+18,", Cumplira 21 años en: ", año+21," y cumplira 100 años en el: ",año+100)

#Ejercicio 2;
segundos = int(input("Ingrese una cantidad de segundos: "))
segundos1 = segundos 
horas = segundos // 3600
segundos = int(segundos % 3600)
minutos = segundos // 60
segundos = int(segundos % 60)
print (segundos1," segundos son: ",horas," horas ",minutos," minutos y ",segundos, "segundos")

#Ejercicio 3;
num = int(input("Ingrese un num para saber su tabla: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#Ejercicio 4; 
N = int(input("Ingrese un numero: "))
for i in range(1,N+1):
    if (i%5) == 0:
        continue
    print(i)

#Ejercicio 5;    
precio = int(input("Ingrese el precio de un producto: "))
total = 0
while True:
    if precio == 0:
        break
    total += precio
    precio = int(input("Ingrese el precio de un producto: "))
    
print("La suma de los valores de los productos es: ",total)

#Ejercicio 6;
Lista = []
Lista2 = []
N = int(input("Ingrese un numero: "))
for i in range(1,N+1):
    if (i%5) == 0:
        Lista.append(i)
    else:
        Lista2.append(i)
print("Numeros: ",Lista2,"\nNumeros multiplo de 5: ",Lista)

#Ejercicio 7;  
oracion = ""
Palabras2 =[]
for i in range(10):
    Palabras2.append(input("Ingrese una palabra: "))
Largas = [pal for pal in Palabras2 if len(pal)>3]
for elem in Largas:
    oracion = oracion + elem + " "
print (oracion)

