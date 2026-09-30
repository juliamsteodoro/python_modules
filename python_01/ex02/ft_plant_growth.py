class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self, amount: float = 0.8) -> None:
        self.height += amount

    def age_one_day(self) -> None:
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    inital_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age_one_day()
        print(f"=== Day {day} ===")
        rose.show()
    growth_this_week: float = round(rose.height - inital_height, 1)
    print(f"Growth this week: {growth_this_week}cm")
