
import os




def run():
    while True:
        os.system('cls')  # Limpia la pantalla al mostrar el menú
        print("Elige una opción:")
        print("1.- Sumar")
        print("2.- Restar")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("5.- Salir")
        
        opcion = int(input("Dame una opción: "))
        
        if opcion == 1:
            function1()
        elif opcion == 2:
            function2()
        elif opcion == 3:
            function3()
        elif opcion == 4:
            function4()
        elif opcion == 5:          
            break
        else:
            print("Opcion no valida")
        input("")


def function1():
    os.system('cls')
    print("Dame dos numeros")
    num1=int(input("Primer numero:"))
    num2=int(input("Segundo numero:"))
    print("La suma de los numero es: ", num1 + num2)

def function2():
    os.system('cls')
    print("Dame dos numeros")
    num1=int(input("Primer numero:"))
    num2=int(input("Segundo numero:"))
    print("La resta de los numero es: ", num1 - num2)


def function3():
    os.system('cls')
    print("Dame dos numeros")
    num1=int(input("Primer numero:"))
    num2=int(input("Segundo numero:"))
    print("La mutliplicación de los numero es: ", num1 * num2)


def function4():
    os.system('cls')
    print("Dame dos numeros")
    num1=int(input("Primer numero:"))
    num2=int(input("Segundo numero:"))
    print("La división de los numero es: ", num1/num2)
run()