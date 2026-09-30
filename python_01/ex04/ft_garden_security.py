class Plant:
    def __init__(self, name: str, height: float, age:  int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        if height < 0:
            print("Erro! Altura não pode ser negativa.")
        else:
            self._height = float(height)
        if age < 0:
            print("Erro! A idade não pode ser negativa.")
        else:
            self.age = int(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print("A altura não pode ser um valor negativo.")
        else:
            self._height = height
            print("Altura atualizada.")

    def set_age(self, age: int) -> None:
        if age < 0:
            print("A idade não pode ser negativa")
        else:
            self._age = age
            print("Idade atualizada.")

    def show(self) -> None:
        print(f"{self._name}:{round(self._height, 1)}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print("Current state: ", end="")
    rose.show()
