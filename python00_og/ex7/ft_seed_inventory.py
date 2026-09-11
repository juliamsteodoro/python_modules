def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()

    if unit == "packets":
        print(seed, "seeds:", quantity, unit, "available")
        return
    elif unit == "grams":
        print(seed, "seeds:", quantity, unit, "total")
        return
    if unit == "area":
        print(seed, "seeds: covers", quantity, "square meters")
        return
    else:
        print("Unknown unit type")
