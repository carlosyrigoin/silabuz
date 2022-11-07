import requests

#ver Pokemones
def ver_pokemones(opcion, url):
  data = requests.get(url).json()
  lista = []
  if opcion == 1:
    lista = data["pokemon_species"]
  elif opcion == 2:
    lista = [{"name": data["pokemon"]["name"]}]
  elif opcion == 3:
    for item in data["pokemon"]:
      lista.append({"name": item["pokemon"]["name"]})
  elif opcion == 4:
    lista = data["pokemon_species"]
  elif opcion == 5:
    for item in data["pokemon"]:
      lista.append({"name": item["pokemon"]["name"]})

  for info in lista:
    url = "https://pokeapi.co/api/v2/pokemon/"+info["name"]
    subdata = requests.get(url).json()
    habilidades = []
    for i in subdata["abilities"]:
      habilidades.append(i['ability']['name'].capitalize())

    print("Nombre:",info["name"])
    print("Habilidades:",habilidades)
    print("Url:",subdata["sprites"]["back_default"],"\n")

  lista_opciones()




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