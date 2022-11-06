import csv



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
