
print("""
=========================
Tarea 01 - BackEnd SILABUZ
=========================
""")

print("Opciones del Programa:\n")
print("Opción 1: Leer libro")
print("Opción 2: Listar libros")
print("Opción 3: Agregar libro")
print("Opción 4: Eliminar libro")
print("Opción 5: Buscar libro por ISBN o título")
print("Opción 6: Ordenar libros por titulo")
print("Opción 7: Buscar libros por autor, editorial o género")
print("Opción 8: Buscar libros numero de autores")
print("Opción 9: Modificar datos de un libro")
print("Opción 10: Guardar libros")

opcion = int(input("SELECCIONE UNA OPCION CON EL NUMERO \n  " ) )

import csv

# LISTAR LIBROS (OPCION 2)
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


if opcion == 1:
    print("libro 1 \n")

    id = input("id ")
    titulo = input(" \n titulo ")
    genero = input("\n genero ")
    isbn = input("\n isbn ")
    editorial = input("\n editorial ")
    autor = input("\n autor ")

    agregarlibro = agregar(id,titulo, genero, isbn,editorial, autor)
    agregarlibro.nuevo()

    print("libro 2 \n")

    id = input("id ")
    titulo = input("\n titulo ")
    genero = input("\n genero ")
    isbn = input("\n isbn ")
    editorial = input("\n editorial ")
    autor = input(" \nautor")

    agregarlibro = agregar(id,titulo, genero, isbn,editorial, autor)
    agregarlibro.nuevo()

    print("libro 3 \n")

    id = input("\n id ")
    titulo = input("\n titulo ")
    genero = input("\n genero ")
    isbn = input("\n isbn ")
    editorial = input("\n editorial ")
    autor = input("\n autor ")

    agregarlibro = agregar(id,titulo, genero, isbn,editorial, autor)
    agregarlibro.nuevo()



elif opcion == 2 :
    listar()


