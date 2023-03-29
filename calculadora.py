import numpy as np 

# Introducir modo de operar
print("MODOS:")
print("1 - sumar")
print("2 - restar")
print()
modo = input("Introduce el método con el que quieras operar:")

if modo == "sumar" or modo == 1: 
    print("estamos sumando")
    #sumar()
elif modo == "restar" or modo == 2:
    print("estamos restando")
    #restar()
    else: 
        exit(0)