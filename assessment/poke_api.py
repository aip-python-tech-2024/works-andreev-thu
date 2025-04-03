from functools import cache
from typing import Generator

from requests import get, Response

from assessment.base_pokemon import BasePokemon
from assessment.poke_error import PokemonError
from assessment.pokemon import Pokemon
from assessment.pokemon_stats import PokemonStats


class PokeAPI:
    BASE_URL = 'https://pokeapi.co/api/v2'

    @classmethod
    @cache
    def get_pokemon(cls, pokemon_id: int | str) -> Pokemon:
        if not isinstance(pokemon_id, (int, str)):
            raise PokemonError('Pokemon ID must be int or str')

        url: str = f'{cls.BASE_URL}/pokemon/{pokemon_id}'
        response: Response = get(url)

        if not response.ok:
            raise PokemonError(f'Pokemon {pokemon_id} not found')

        data: dict = response.json()

        stats: PokemonStats = PokemonStats(
            hp=data['stats'][0]['base_stat'],
            attack=data['stats'][1]['base_stat'],
            defense=data['stats'][2]['base_stat'],
            special_attack=data['stats'][3]['base_stat'],
            special_defense=data['stats'][4]['base_stat'],
            speed=data['stats'][5]['base_stat'],
        )

        return Pokemon(
            id=data['id'],
            name=data['name'],
            weight=data['weight'],
            height=data['height'],
            stats=stats,
        )

    @classmethod
    def get_all(cls, get_full: bool = False) -> Generator[BasePokemon | Pokemon, None, None]:
        if not isinstance(get_full, bool):
            raise PokemonError('get_full must be bool')

        url: str = f'{cls.BASE_URL}/pokemon'
        while url is not None:
            response: Response = get(url)
            data: dict = response.json()
            for pokemon in data['results']:
                if get_full:
                    yield cls.get_pokemon(pokemon['name'])
                else:
                    yield BasePokemon(name=pokemon['name'])
            url = data['next']


print(PokeAPI.get_pokemon('ditto'))

pokemons = []
for i, pokemon in enumerate(PokeAPI.get_all(get_full=True), 1):
    print(pokemon)
    pokemons.append(pokemon)

    if i == 50:
        break

print(max(pokemons, key=lambda pokemon: pokemon.weight))
