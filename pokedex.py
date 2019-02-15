import requests
import json

poke_list = json.loads(requests.get("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json").text)

pokemon_names = [(pokemon["name"]) for pokemon in poke_list
          if (pokemon["name"])]

pokemon_names_eng = [str(pokemon_eng["english"]) for pokemon_eng in pokemon_names
          if str(pokemon_eng["english"])]

# print(poke_list)
# print(pokemon_names)
# print(pokemon_names_eng)

# print(pokemon_names_eng[x-1])
