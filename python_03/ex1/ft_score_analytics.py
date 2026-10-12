import sys

def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    length = len(sys.argv) - 1
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print(f"No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores) / len(scores))}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {(max(scores) - min(scores))}")

if __name__ == "__main__":
    main()