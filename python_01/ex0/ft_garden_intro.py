#!/usr/bin/env python3

def ft_garden_intro() -> None:
    plant: str = "Rose"
    height: float = 25
    age: int = 30
    print(f"Plant: {plant}\nHeight: {height}cm\nAge: {age} days\n")


def main() -> None:
    print("=== Welcome to My Garden ===")
    ft_garden_intro()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
