import json

def read_json_file(pokemons_file):
    with open(pokemons_file, "r", encoding="utf-8") as file:
        return json.load(file)


def add_new_pokemon(pokemon_list):
    while True:
        pokemon = {
            "name": {
                "english": input("Ingrese el nombre del Pokémon: ")
            },
            "level": int(input("Ingrese el nivel: ")),
            "type": [input("Ingrese el tipo: ")],
            "base": {
                "HP": int(input("HP: ")),
                "Attack": int(input("Ingrese el ataque: ")),
                "Defense": int(input("Ingrese la defensa: ")),
                "Sp. Attack": int(input("Ingrese el Sp. Attack: ")),
                "Sp. Defense": int(input("Ingrese el Sp. Defense: ")),
                "Speed": int(input("Ingrese la velocidad: "))
            }
        }

        pokemon_list.append(pokemon)

        again = input("¿Desea agregar otro Pokémon? (si/no): ").lower()
        if again != "si":
            break


def write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)



pokemon_list = read_json_file("pokemon.json")
add_new_pokemon(pokemon_list)
write_json_file("pokemon.json", pokemon_list)