import random
import string

words = {"Lenguajes" : ["python"],
        "Conceptos de programacion" : ["variable","funcion","bucle","programa"],
        "Tipos de datos" : ["cadena", "entero", "lista"]}

while True:
    print("Categorias disponibles: ",words.keys())  #Mostrar las categorias disdponibles
    categoria = input("Ingrese que categoria desea: ")

    if categoria in words:
        word = random.choice(words[categoria])
        break
    else:
        print("Categoria desconocida.")

guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje += 6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    #SOLUCION DEL BuG 7.1;
    if len(letter) != 1 or letter not in string.ascii_letters:
        print("Entrada no valida.")

    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -=1
        print("Esa letra no está en la palabra.")

    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0

print (f"Puntaje: {puntaje}")