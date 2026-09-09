def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalizer()

    if unit is "packets":
        print(seed, "seeds:", quantity, unit, "available")
    if unit is "grams":
        print(seed, "seeds:", quantity, unit, "total")
    if unit is "area":
        print(seed, "seeds: covers", quantity, "square meters")