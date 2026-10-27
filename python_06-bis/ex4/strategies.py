from abc import ABC, abstractmethod
from ex3.capabilities import TransformCapability
from ex3.creatures import Creature


class IncompatibleStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Normal Strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise IncompatibleStrategyError(
                "Normal strategy requires a Creature"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Aggressive Strategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise IncompatibleStrategyError(
                f"Invalid Creature '{creature.name}' for aggressive strategy"
            )
        t_msg = creature.transform()
        try:
            a_msg = creature.attack()
        finally:
            r_msg = creature.revert()
        return f"{t_msg}\n{a_msg}\n{r_msg}"
