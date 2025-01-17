from io import open

text="Una line"
#La w es para especificar que es de escritura
archivo=open("archivo.txt","w")
archivo.write(text)
text="\nna line nueva"
archivo.write(text)
text="\nna line nuevaaa"
archivo.write(text)
archivo.close()