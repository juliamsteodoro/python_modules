from abc import ABC, abstractmethod
from ex3.creatures import (
    Creature,
    Flameling,
    Morphagon,
    Pyrodon,
    Shiftling,
)


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Cria e retorna a criatura em sua forma base."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Cria e retorna a criatura em sua forma evoluída."""
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()