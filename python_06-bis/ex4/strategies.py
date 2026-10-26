from abc import ABC, abstractmethod
from ex3.capabilities import TransformCapability
from ex3.creatures import Creature


class IncompatibleStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def execute(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Normal Strategy")

    def execute(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Aggressive Strategy")

    def execute(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise IncompatibleStrategyError(
                f"{creature.name} lacks TransformCapability for Aggressive Strategy!"
            )

        t_msg = creature.transform()
        a_msg = creature.attack()
        r_msg = creature.revert()
        return f"{t_msg}\n{a_msg}\n{r_msg}"