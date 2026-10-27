from ex3 import TransformCreatureFactory


def test_transform_capability() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if hasattr(base, "transform") and hasattr(base, "revert"):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if hasattr(evolved, "transform") and hasattr(evolved, "revert"):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    test_transform_capability()
