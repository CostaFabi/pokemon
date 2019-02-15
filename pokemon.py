from pokedex import pokemon_names_eng

def number(day, month, name):
    result = ((day * month) * len(name))

    n = int(result)


    while n > 809:
        n //= 2

        if n <= 809:
            break

    return(n)

poke_number = number(1, 7, 'myrian')  #Insert(day, month, 'name')
your_pokemon = pokemon_names_eng[poke_number - 1]

print('#', poke_number, your_pokemon)
