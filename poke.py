import random
import requests
from pokemons_list import pokemon_list

def randomize_poke(pokemon_list):
    return random.choice(pokemon_list)

def get_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    color_url = f"https://pokeapi.co/api/v2/pokemon-species/{nome.lower()}"

    resp = requests.get(url)
    resp_color = requests.get(color_url)

    if resp.status_code == 200:
        data = resp.json()
        color_data = resp_color.json()
        name = data["name"]
        types = [tipo["type"]["name"] for tipo in data["types"]]
        color = color_data["color"]["name"]
        weight = data["weight"]
        height = data["height"]
        habilities = [hab["ability"]["name"] for hab in data["abilities"]]

        return {
            "name": name,
            "types": types,
            "color": color,
            "weight": weight,
            "height": height,
            "habilities": habilities
        }

def check_types(secret, choice):
    som = 0
    for type_s in secret["types"]:
        for type_c in choice["types"]:
            if type_s == type_c:
                som += 1
    return som

def check_hab(secret, choice):
    som = 0
    for hab_s in secret["habilities"]:
        for hab_c in choice["habilities"]:
            if hab_s == hab_c:
                som += 1
    return som

def compair(secret, choice):
    try:
        if secret["name"] == choice["name"]:
            print(f"Parabéns!! você acertou o pokemon secreto, era o {secret['name']}!")
            return 1
        else:
            if secret["types"] == choice["types"]:
                print(f"Tipo - {', '.join(choice['types'])}: ✅")
            else:   
                if check_types(secret, choice) > 0:
                    print(f"Tipo - {', '.join(choice['types'])}: 🟡")
                else:
                    print(f"Tipo - {', '.join(choice['types'])}: ❌")

            if secret["color"] == choice["color"]:
                print(f"Cor - {choice['color']}: ✅")
            else:
                print(f"Cor - {choice['color']}: ❌")

            if secret["weight"] == choice["weight"]:
                print(f"Peso - {choice['weight']}: ✅")
            elif secret["weight"] > choice["weight"]:
                print(f"Peso - {choice['weight']}: 🔼")
            else:
                print(f"Peso - {choice['weight']}: 🔽")
            
            if secret["height"] == choice["height"]:
                print(f"Altura - {choice['height']}: ✅")
            elif secret["height"] > choice["height"]:
                print(f"Altura - {choice['height']}: 🔼")
            else:
                print(f"Altura - {choice['height']}: 🔽")

            if secret["habilities"] == choice["habilities"]:
                print(f"Habilidades - {', '.join(choice['habilities'])}: ✅")
            else:
                if check_hab(secret, choice) > 0:
                    print(f"Habilidades - {', '.join(choice['habilities'])}: 🟡")
                else:
                    print(f"Habilidades - {', '.join(choice['habilities'])}: ❌")
    except Exception as e:
        print(f"Erro!\n")
        return 0
    print("\n")

if __name__ == "__main__":
    secret = randomize_poke(pokemon_list)
    secret_atributes = get_pokemon(secret)
    print("------- Bem-Vindo ao jogo que não é cópia do Pokedle ------- \n")

    while True:
        pokemon = input("Digite um pokemon: ").lower().strip()
        if pokemon not in pokemon_list:
            print("Pokemon não encontrado!\n")
            continue
        choice = get_pokemon(pokemon)

        if compair(secret_atributes, choice) == 1:
            break
