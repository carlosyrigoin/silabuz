import requests

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
  if opcion == 1:
    url = "https://pokeapi.co/api/v2/generation/"
    data = requests.get(url).json()
    print("\n\nGeneraciones de pokemones:\n")
  elif opcion == 2:
    url = "https://pokeapi.co/api/v2/pokemon-form/"
    data = requests.get(url).json()
    print("\n\Formas de pokemones:\n")
  elif opcion == 3:
    url = "https://pokeapi.co/api/v2/ability/"
    data = requests.get(url).json()
    print("\n\Habilidades de pokemones:\n")
  elif opcion == 4:
    url = "https://pokeapi.co/api/v2/pokemon-habitat/"
    data = requests.get(url).json()
    print("\n\Habitad de pokemones:\n")
  elif opcion == 5:
    url = "https://pokeapi.co/api/v2/type/"
    data = requests.get(url).json()
    print("\n\Tipos de pokemones:\n")
  else:
    print("Muchas gracias !!!")
  
  if opcion in (1,2,3,4,5):
    for item, info in enumerate(data['results'], start = 1):
      print("   ",item,":",info["name"])
    print("    0 : Regresar al menú principal\n")
    subopcion = int(input("Ingresar generación a listar => "))
    if subopcion == 0:
      lista_opciones()
    else:
      ver_pokemones(opcion, url+str(subopcion))

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