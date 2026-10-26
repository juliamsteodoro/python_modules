from ex3 import FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    IncompatibleStrategyError,
    NormalStrategy,
)


def run_match(
    creature_name: str,
    creature_obj: object,
    strategy: BattleStrategy
) -> None:
    print(f"Applying {strategy.name} to {creature_name}:")
    try:
        result = strategy.execute(creature_obj)  # type: ignore
        print(result)
    except IncompatibleStrategyError as e:
        print(f"Strategy Error: {e}")
    print()


if __name__ == "__main__":
    print("=== Code Nexus - Tournament ===\n")

    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    flameling = flame_factory.create_base()
    shiftling = transform_factory.create_base()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()

    run_match(flameling.name, flameling, normal_strat)

    run_match(flameling.name, flameling, aggressive_strat)

    run_match(shiftling.name, shiftling, aggressive_strat)