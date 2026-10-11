class GardenError(Exception):
    def __init__(self, message: str = "Graden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
     def __init__(self, message: str = "A plant error occurred" ) -> None:
        super().__init__(message)


class WaterError(GardenError):
     def __init__(self, message: str = "A water error occurred" ) -> None:
        super().__init__(message)


def custom_erros() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as plant_error:
        print(f" Caught PlantError: {plant_error}")

    print("Testing WaterError...")
    try:
        raise WaterError(" Not enough water in the tank!")
    except WaterError as water_error:
        print(f"Caught WaterError: {water_error}")
    
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
            print(f"Caught GardenError: {error}")
    try:
        raise WaterError(" Not enough water in the tank!")
    except GardenError as error:
            print(f"Caught GardenError: {error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    custom_erros()



    