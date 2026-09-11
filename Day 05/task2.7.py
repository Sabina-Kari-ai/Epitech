item = input("pokemon: ")
types = {
    "Electric": ["Pikachu"],
    "Grass": ["Bulbasaur", "Leafeaon"],
    "Fire": ["Charmender", "Scovillain"]
}

for pokemon_type in types:
    if item in types[pokemon_type]:
        print(pokemon_type)