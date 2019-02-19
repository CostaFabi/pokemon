import requests
import json

pokedex = json.loads(requests.get("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json").text)

def number(day, month, name):
    result = ((day * month) * len(name))

    n = int(result)

    while n > len(pokedex):
        n //= 2

    return(n)

poke_number = number(26, 7, 'fabio')  #Insert(day, month, 'name')
your_pokemon = pokedex[poke_number - 1]['name']['english']

print('#', poke_number, your_pokemon)
