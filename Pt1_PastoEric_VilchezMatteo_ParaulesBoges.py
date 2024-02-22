"""
    Eric Pasto i Matteo Vilchez.
    22/02/2024
    ASIXc 1B  M03 UF2 A1
    ParaulesBoges Pt.1
    Fer un programa que demani una frase per teclat i la retorni per pantalla
    amb les lletres de cada paraula de la frase desordenada
"""
#1 Pedir un texto
#1.2 Tener en cuenta los caracteres especiales
#2 Separamos cada palabra de la frase para que se desordene
#3 Desordenar la frase teniendo en cuenta que la primera y ultima letra no se mueven
#4 Devolvemos toddo el texto desordenado
#5 Escribimos un "quiere decir" y ahí mostrará el texto original que mandó el usuario

texto_ord = []
cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]
def frase():
    texto = input("Dime el texto a desordenar: ")
    texto_ord=texto.split
    return texto,texto_ord
def desordenar_palabras():
    for palabrades in texto_ord:
     pLetra = palabrades[0]
     uLetra = palabrades[-1]
     print(pLetra)
     print(uLetra)

frase()
desordenar_palabras()
print(texto_ord)
