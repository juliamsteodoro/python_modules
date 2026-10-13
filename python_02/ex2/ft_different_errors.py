def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/ghost.txt")
    elif operation_number == 3:
        "plant" + 1  # type: ignore[operator]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in (0, 1, 2, 3, 4):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError, TypeError) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
        except ZeroDivisionError as divided_zero:
            print(f"Caught ZeroDivisionError: {divided_zero}")
        except FileNotFoundError as not_found_file:
            print(f"Caught FileNotFoundError: {not_found_file}")
        else:
            print("Operation completed successfully")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
