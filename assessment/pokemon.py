from dataclasses import dataclass

from assessment.base_pokemon import BasePokemon
from assessment.pokemon_stats import PokemonStats


@dataclass(frozen=True)
class Pokemon(BasePokemon):
    id: int
    weight: int
    height: int
    stats: PokemonStats
