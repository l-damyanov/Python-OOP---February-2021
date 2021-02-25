from pokemon_battle.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon_n: Pokemon):
        if pokemon_n in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon_n)
        return f"Caught {pokemon_n.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        filtered_pokemon = [p for p in self.pokemon if p.name == pokemon_name]
        if filtered_pokemon:
            p = filtered_pokemon[0]
            self.pokemon.remove(p)
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            result += f"- {p.pokemon_details()}\n"
        return result
