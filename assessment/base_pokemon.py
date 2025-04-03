from dataclasses import dataclass


@dataclass(frozen=True)
class BasePokemon:
    name: str
