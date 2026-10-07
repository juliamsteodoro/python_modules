class Plant:

    class Stats:

        def __init__(self) -> None:
            self._age_calls: int = 0
            self._show_calls: int = 0
            self._grow_calls: int = 0

        def log_grow(self) -> None:
            self._grow_calls += 1

        def log_age(self) -> None:
            self._age_calls += 1

        def log_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = float(height)
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = int(age)
        self.stats = self.Stats()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def grow(self, amount: float) -> None:
        self._height += amount
        self.stats.log_grow()

    def age(self, days: int) -> None:
        self._age += days
        self.stats.log_age()

    def show(self) -> None:
        self.stats.log_show()
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0.0, age=0)


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int,
    ) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            print(f" Seeds: {self.seed_count}")
        else:
            print(" Seeds: 0")


class Tree(Plant):

    class Stats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def log_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

        self.stats: Tree.Stats = self.Stats()

    def produce_shade(self) -> None:
        self.stats.log_shade()
        height_str = f"{round(self._height, 1)}cm"
        diam_str = f"{round(self.trunk_diameter, 1)}cm"
        print(
            f"Tree {self._name} now produces a shade of "
            f"{height_str} long and {diam_str} wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


def display_plant_analytics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_analytics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_analytics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_analytics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_analytics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", seed_count=42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_analytics(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_analytics(anonymous)
