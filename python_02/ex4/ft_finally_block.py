class PlantError(Exception):
    def __init__(self, message: str = "Invalid plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    try:
        print("Opening watering system")
        print("Testing valid plants...")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
        print("\nTesting invalid plants...")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(
            f"Caught PlantError: {error}... "
            "ending tests and returning to main"
        )
        return
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
