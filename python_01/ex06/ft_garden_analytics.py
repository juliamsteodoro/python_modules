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

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.Stats()

    def grow(self, amount: float) -> None:
        self.height += amount
        self.stats.log_grow()

    def plant_age(self, days: int) -> None:
        self.age += days
        self.stats.log_age()

    def show(self) -> None:
        self.stats.log_show()
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name="Anonymous Plant", height=0.0, age=0)


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")


class Seed(Flower):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seed_count: int,
    ):
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            print(f"Seeds available: {self.seed_count}")
        else:
            print("Seeds: Has not bloomed yet")


class Tree(Plant):

    class Stats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def log_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"- Shade calls: {self._shade_calls}")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

        self.stats: Tree.Stats = self.Stats()

    def produce_shade(self) -> None:
        self.stats.log_shade()
        height_str = f"{round(self.height, 1)}cm"
        diam_str = f"{round(self.trunk_diameter, 1)}cm"
        print(
            f"Tree {self.name} now produces a shade of "
            f"{height_str} long and {diam_str} wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


def display_plant_analytics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
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

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_analytics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(5.0)
    rose.bloom()
    rose.show()
    display_plant_analytics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    display_plant_analytics(oak)

    print("=== Seed (inherits Flower)")
    sunflower = Seed("Sunflower", 30.0, 45, "yellow", seed_count=100)
    sunflower.show()
    sunflower.bloom()
    sunflower.show()
    display_plant_analytics(sunflower)
