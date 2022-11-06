import csv





#OPCION 3
#AGREGAR LIBRO
class agregar:
    def __init__(self,id,titulo, genero, isbn,editorial, autor):
        self.id =id
        self.titulo= titulo
        self.genero= genero
        self.isbn= isbn
        self.editorial= editorial
        self.autor= autor

    def nuevo(self):
        nuevolibro =[str(self.id), str(self.titulo), str(self.genero),  str(self.isbn), str(self.editorial),str(self.autor)]

        with open("libros.csv", "a", newline="") as myfile:
            escribir = csv.writer(myfile)
            escribir.writerow(nuevolibro)
            myfile.close()






#OPCION 7

# BUSCAR LIBRO POR AUTOR
def buscarlibro_autor(valor):
    numero= 0
    autor= []

    with open ("libros.csv", encoding= "utf-8") as f:
        archivo = csv.reader(f)
        datos= []
        next(archivo) # hace que el objeto iterador se mueva 1 ( no se ve el titulo)
    
        for lista in archivo:
            autor.append(lista[5])
            datos.append(lista)
        
            if autor[numero] == valor:
                print(datos[numero])
            numero= numero + 1
        f.close()


#BUSCAR LIBRO POR EDITORIAL
def buscarlibro_editorial(valor):
    numero= 0
    editorial= []

    with open ("libros.csv", encoding= "utf-8") as f:
        archivo = csv.reader(f)
        datos= []
        next(archivo) # hace que el objeto iterador se mueva 1 ( no se ve el titulo)
    
        for lista in archivo:
            editorial.append(lista[4])
            datos.append(lista)
        
            if editorial[numero] == valor:
                print(datos[numero])
            numero= numero + 1
        f.close()


#BUSCAR LIBRO POR GENERO
def buscarlibro_genero(valor):
    numero= 0
    genero= []

    with open ("libros.csv", encoding= "utf-8") as f:
        archivo = csv.reader(f)
        datos= []
        next(archivo) # hace que el objeto iterador se mueva 1 ( no se ve el titulo)
    
        for lista in archivo:
            genero.append(lista[2])
            datos.append(lista)
        
            if genero[numero] == valor:
                print(datos[numero])
            numero= numero + 1
        f.close()
