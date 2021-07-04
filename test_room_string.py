#!/usr/bin/env python
# -*- coding: cp1252 -*-

from string import ascii_letters
print(ascii_letters)
x1="{} es el primer valor, {} el segundo y {} el tercero"
print (x1.format("1er", "2do", "3ro")) #formateo de strings
txt="-"
x2=txt.join("123456") #coloca un texto - en el intermedio
print(x2) #union de strings
x3="Esto es un párrafo"
print(x3[::-1]) #invierte el string
print(x3[2:]) #imprime del caracter 2 hasta el final
print(x3.split( )) #separa en vectores una oración
print(x3.replace(" ","-")) #reemplaza un parametro por otro
print(x3.strip("Esto")) #eliminar
print(x3.strip("Esto")) #eliminar
print(x3.lower()) #pone en minusculas
print(x3.encode("ascii","ignore")) #codifica
print(x3.startswith("Esto")) #dice si comienza, devuelve un True
print(x3.find("á")) #dice el lugar donde está el valor
#print(x3.decode("ascii","ignore"))
print(x3.upper()) #pone en mayúsculas
print(x3.endswith("afo")) #dice si termina, devuelve un True
print(x3.rstrip("fo")) #remueve al final, se usa para puntos o comas, o espacios
print(x3.splitlines()) #divine en líneas si tiene el /n
print(x3.count("s")) #cuenta la cantidad de veces que está
print(x3.index("á")) #es igual que find, pero si no lo encuentra hace una excepción
print(x3.isdigit()) #dice si es un dígito
print(x3.lstrip("E")) #remueve el inicio
print(x3.zfill(25)) #rellena con 0 los espacios faltantes
print(x3.ljust(30,"*")) #rellena a la derecha con los caracteres restantes
print(x3.title()) #imprime todas las palabras con el inicio en mayúsculas
print(ord("A")) # indica el valor ascii de A
print(ord("Z")) # indica el valor ascii de Z
print(3*"Hola") # indica Hola 3 veces
print(None==None) # none es como null
# formato string
nums=[4,5,6]
msg="Numbers: {0} {1} {2}".format(nums[0],nums[1],nums[2])
print(msg)
print("{0}{1}{0}".format("abra", "cad"))
# tratamiento de strings
print("Hello ME".replace("ME","world"))
print("This is a sentence.".startswith("This")) #True, es verdadero, termina así
print("This is a sentence.".endswith("sentence.")) #True, es verdadero, comienza así
print("This is a sentence.".upper()) #cambia a mayúsculas
print("An all caps sentence".lower()) #cambia a minúsculas
print("spam, eggs, ham".split(", "))
a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)
