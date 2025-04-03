from dataclasses import dataclass


@dataclass(frozen=True)
class PokemonStats:
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
