import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    length = (len(sys.argv) - 1)
    if length == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length}")
        for i, arg in enumerate(sys.argv[1:]  , start=1):
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {length + 1}")


if __name__ == "__main__":
    main()