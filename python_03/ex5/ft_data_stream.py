import random
from typing import Generator

players = ["alice", "bob", "charlie", "dylan"]
actions = [
    "move", "run", "eat", "sleep", "grab",
    "climb", "swim", "use", "release"
]

def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx = random.randint(0, len(event_list) - 1)
        event = event_list.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {player} did action {action}")
    events = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")

if __name__ == "__main__":
  main()

