import requests

def listar_pokemones(opcion):
  pass

def lista_opciones():
  print("\nOpciones del programa:")
  print("""
    1 : Listar Pokemons por generación
    2 : Listar Pokemons por forma
    3 : Listar Pokemons por habilidad
    4 : Listar Pokemons por habitad
    5 : Listar Pokemons por tipo
    0 : Cerrar programa
  """)
  opcion = int(input("Ingresar opción => "))
  listar_pokemones(opcion)

print("\n******************************************\n\tTarea 02 - Backend SILABUZ\n******************************************")
lista_opciones()