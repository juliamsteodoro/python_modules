import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(',')
        coords: list[float] = []
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        for item in parts:
            try:
                coords.append(float(item))
            except ValueError as error:
                print(f"Error on parameter '{item}': {error}")
                break
        if len(coords) == 3:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_zero = math.sqrt((x1)**2 + (y1)**2 + (z1)**2)
    print(f"Distance to center: {round(distance_zero, 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    distance_two = math.sqrt((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance_two, 4)}")


if __name__ == "__main__":
    main()
