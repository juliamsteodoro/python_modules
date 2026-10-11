def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)

def test_temperature() -> None:
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp} °C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        temp = input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()



        
