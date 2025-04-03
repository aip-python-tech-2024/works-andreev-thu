class BasePokemon:
    _name: str

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f'BasePokemon({self._name})'
