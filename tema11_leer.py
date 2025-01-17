from io import open
text=""
#La w es para especificar que es de escritura
archivo=open("archivo.txt","r")
text=archivo.readline()
print(text)
#archivo.readlines()
#archivo.seek(0)
text=archivo.read()
print(text)
archivo.close()