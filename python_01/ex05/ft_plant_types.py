class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.age} days old.\n"
            f"Color: {self.color}"
        )


class Tree(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide"
        )

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.age} days old.\n"
            f"Trunk Diameter: {self.trunk_diameter}cm"
        )


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self.age} days old.\n"
            f"Harvest Season: {self.harvest_season}\n"
            f"Nutritional Value: {self.nutritional_value}"
        )

    def grow(self, amount: float) -> None:
        self.height += amount

    def plant_age(self, days: int) -> None:
        self.age += days
        self.nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.plant_age(20)
    tomato.show()
