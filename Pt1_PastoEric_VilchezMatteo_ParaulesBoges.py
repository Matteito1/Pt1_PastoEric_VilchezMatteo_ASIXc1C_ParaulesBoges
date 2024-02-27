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
#5 Escribimos un "Traducido ordenado" y ahí mostrará el texto original que mandó el usuario

import random
cEspeciales = [".", ",", "?", ":", ";", "!", "'", "¡", "¿"]
#letras=('a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z')
Texto_Ordenado=[]
palabras=[]
frase_Desordenado=[]
def frase():
    try:
        frase=input("Introduce el texto que quieres desordenar: ")
        frase_ordenada=frase.split()
        return frase_ordenada,frase
    except:
        print("Error - Lo que has introducido es incorrecto")
def separar():
    for palabrades in Texto_Ordenado:
        if len(palabrades)>=3:
            if palabrades[-1] in frase:
                sep=list(palabrades[1:-1])
                random.shuffle(sep)
                separado=palabrades[0]+''.join(sep)+palabrades[-1]
            else:
                sep=list(palabrades[1:-2])
                random.shuffle(sep)
                separado=palabrades[0]+''.join(sep)+palabrades[-2]+palabrades[-1]
        else:
            separado=palabrades
        palabras.append(separado)
    return palabras

def juntar():
    frasedes=' '.join(palabras)
    return frasedes
def resultado():
    print(frase_Desordenado)
    print("Texto ordenado:")
    print(frase)

Texto_Ordenado,frase=frase()
palabras=separar()
frase_Desordenado=juntar()
resultado()
