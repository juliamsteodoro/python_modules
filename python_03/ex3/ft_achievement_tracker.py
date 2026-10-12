import random
def gen_player_achievements() ->set[str]:
    achievements_list: list[str] = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Unstoppable",
        "Hidden Path Finder",
    ]
    count = random.randint(4, 8)
    selected = set(random.sample(achievements_list, count))
    return selected

def main() -> None:
    print("=== Achievement Tracker System ===")
    players = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements(),
}

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    distint = set.union(*players.values())
    print(f"\nAll distinct achievements: {distint}")

    common = set.intersection(*players.values())
    print(f"\nCommon achievements: {common}")

    for name, achievements in players.items():
        others = set.union(*[s for k, s in players.items() if k != name])
        only_player = achievements.difference(others)
        print(f"Only {name} has: {only_player}")
        missing = distint.difference(achievements)
        print(f"{name} is missing: {missing}")

if __name__ == "__main__":
    main()

