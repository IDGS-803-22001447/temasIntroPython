
from io import open

class Traductor:
    def __init__(self, archivo="traductor.txt"):
        self.archivo = archivo
        self.diccionario = [] 

    def guardar_palabra(self, espanol, ingles):
    
        self.diccionario.append((espanol, ingles))
   
        archivo = open(self.archivo, "a")  
        archivo.write("{},{}\n".format(espanol, ingles)) 
        archivo.close()  
        print("Palabra agregada correctamente.")


    def buscar_palabra(self, palabra, idioma):
    
        archivo = open(self.archivo, "r")
        lineas = archivo.readlines()
        for linea in lineas:
            espanol, ingles = linea.strip().split(",")
            if idioma == "espanol" and palabra.lower() == espanol.lower():
                archivo.close()
                return "Palabra encontrada: {}".format(ingles)
            elif idioma == "ingles" and palabra.lower() == ingles.lower():
                archivo.close()
                return "Palabra encontrada: {}".format(espanol)

                archivo.close()
                return "Palabra no encontrada"


def main():
    traductor = Traductor()

    while True:
        print("\nMenú Principal:")
        print("1. Capturar palabras")
        print("2. Buscar palabras")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            espanol = input("Ingresa la palabra en español: ")
            ingles = input("Ingresa la palabra en inglés: ")
            traductor.guardar_palabra(espanol, ingles)

        elif opcion == "2":
            idioma_opcion = input("Buscar en: 1. Español, 2. Inglés: ")
            if idioma_opcion == "1":
                palabra = input("Ingresa la palabra en español: ")
                print(traductor.buscar_palabra(palabra, "espanol"))
            elif idioma_opcion == "2":
                palabra = input("Ingresa la palabra en inglés: ")
                print(traductor.buscar_palabra(palabra, "ingles"))
            else:
                print("Opción no válida")

        elif opcion == "3":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
