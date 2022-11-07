import csv

def listar():
    with open("libros.csv", encoding="utf-8") as f:
        archivo = csv.reader(f)
        datos = []
        next(archivo)  # hace que el objeto iterador se mueva 1 ( no se ve el titulo)

        # listar libros
        for i in archivo:
            datos.append(i)
        for dato in datos:
            print(dato)
    f.close()

def buscarlibro_isbn(valor):
    numero = 0
    ibsn = []

    with open("libros.csv", encoding="utf-8") as f:
        archivo = csv.reader(f)
        datos = []
        next(archivo)  # hace que el objeto iterador se mueva 1 ( no se ve el titulo)

        for lista in archivo:
            ibsn.append(lista[3])
            datos.append(lista)

            if int(ibsn[numero]) == valor:
                print(datos[numero])
            numero = numero + 1
        f.close()

class agregar:
    def __init__(self, id, titulo, genero, isbn, editorial, autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def nuevo(self):
        nuevolibro = [str(self.id), str(self.titulo), str(self.genero), str(self.isbn), str(self.editorial),
                      str(self.autor)]

        with open("libros.csv", "a", newline="") as myfile:
            escribir = csv.writer(myfile)
            escribir.writerow(nuevolibro)
            myfile.close()

def seleccionar_opcion(opcion):
    if opcion == 2:
        listar()
    elif opcion == 3:
        id = input("id ")
        titulo = input("titulo ")
        genero = input("genero ")
        isbn = input("isbn ")
        editorial = input("editorial ")
        autor = input("autor ")

        agregarlibro = agregar(id, titulo, genero, isbn, editorial, autor)
        agregarlibro.nuevo()
    elif opcion == 4:
        nombre_archivo = 'libros.csv'

        with open(nombre_archivo, newline='') as f:
            datos = csv.reader(f, delimiter='\t')
            libros = list(datos)

            position = int(input("Escribir index:"))
            libros.pop(int(position))
            print(libros)
        f.close()
    elif opcion == 5:
        valor = int(input("isbn "))
        buscarlibro_isbn(valor)
    elif opcion == 8:
        with open("libros.csv", encoding="utf-8") as f:
            archivo = csv.reader(f)
            next(archivo)
            autores = []

            for lista in archivo:
                autores.append(lista[5])

            autores_filtrados = []

            for autores2 in autores:
                if autores2 != ' ':
                    autores_filtrados.append(autores2)

            print(autores_filtrados)
    else:
        print("Muchas gracias !!!")

def lista_opciones():
    print("\nOpciones del programa:")
    print("""
        1 : Leer libro
        2 : Listar libros
        3 : Agregar libro
        4 : Eliminar libro
        5 : Buscar libro por ISBN o título
        6 : Ordenar libros por titulo
        7 : Buscar libros por autor, editorial o género
        8 : Buscar libros numero de autores
        9 : Modificar datos de un libro
        10: Guardar libros
        0 : Cerrar programa
    """)
    opcion = int(input("Ingresar opción => "))
    seleccionar_opcion(opcion)

print("\n******************************************\n\tTarea 01 - Backend SILABUZ\n******************************************")
lista_opciones()