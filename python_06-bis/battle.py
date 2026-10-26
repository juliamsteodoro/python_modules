from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(f"{c1.describe()} vs.")
    print(f"{c2.describe()} fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    print("=== Code Nexus - Battle Sandbox ===\n")

    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    test_factory(flame_factory)
    test_factory(transform_factory)

    test_battle(flame_factory, transform_factory)