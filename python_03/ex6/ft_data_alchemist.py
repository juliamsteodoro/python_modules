import random

players: list[str] = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam',
]

def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    capitalized: list[str] = [
        name.capitalize() for name in players
    ]
    print(f"New list with all names capitalize: {capitalized}")
    capitalizedOnly: list[str] = [
        name for name in players if name.istitle()
    ]
    print(f"New list of capitalized names only: {capitalizedOnly}")

    scores: dict[str, int] = {
        name: random.randint(1, 1000) for name in capitalized
    }
    print(f"Score dict: {scores}")
    avg_score: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg_score}")
    highScores: dict[str, int] = {
        name: score for name, score in scores.items() if score > avg_score
    }
    print(f"High scores: {highScores}")


if __name__ == "__main__":
    main()