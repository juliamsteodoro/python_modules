from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    IncompatibleStrategyError,
    NormalStrategy,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    participants = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]
    for index, (first, first_strategy) in enumerate(participants):
        for second, second_strategy in participants[index + 1:]:
            print("\n* Battle *")
            print(first.describe())
            print(" vs.")
            print(second.describe())
            print(" now fight!")
            try:
                for creature, strategy in (
                    (first, first_strategy), (second, second_strategy)
                ):
                    if not strategy.is_valid(creature):
                        raise IncompatibleStrategyError(
                            f"Invalid Creature '{creature.name}' "
                            f"for {strategy.name}"
                        )
                    print(strategy.act(creature))
            except IncompatibleStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame_factory, normal), (transform_factory, aggressive)])

    print("\nTournament 1 (error)")
    battle([(transform_factory, aggressive), (flame_factory, aggressive)])
