#!/usr/bin/env python3

class Plant:
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

        print(
            f"Plant created: {self._name}: "
            f"{round(self._height, 1)}cm, {self._age} days old"
        )

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
            print(f"Height updated: {int(height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {age} days")

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print()

    rose.set_height(25.0)
    rose.set_age(30)
    print()

    rose.set_height(-10.0)
    rose.set_age(-5)
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
