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