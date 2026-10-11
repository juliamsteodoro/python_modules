def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 1/0
    elif operation_number == 2:
        open("/ghost.txt")
    if operation_number == 3:
        "plant" + 1

def test_error_types() -> None:
    for i in range(4):
        try:
            garden_operations(i)
        except ValueError as bad_data:
            print(f"Caught ValueError: {bad_data}")
        except ZeroDivisionError as divided_zero:
            print(f"Caught ZeroDivisionError: {divided_zero}")
        except TypeError as type_error:
            print(f"Caught TypeError: {type_error}")
        except FileNotFoundError as not_found_file:
            print(f"Caught FileNotFoundError: {not_found_file}")

if __name__ == "__main__":
    test_error_types()