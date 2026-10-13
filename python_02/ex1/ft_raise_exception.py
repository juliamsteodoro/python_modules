def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temperature = int(temp_str)
    if 0 <= temperature <= 40:
        return temperature
    elif temperature < 0:
        raise ValueError(f"{temperature} is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"{temperature} is too hot for plants (max 40°C)")


def test_temperature(temperature_testing: str) -> None:
    try:
        temp = input_temperature(temperature_testing)
        print(f"Temperature now is {temp}")
    except ValueError as input_error:
        print(f"Caught input_temperature error: {input_error}")


def main() -> None:
    print("=== Garden Temperature Checker ===")

    test_temperature("25")
    test_temperature("abc")
    test_temperature("-50")
    test_temperature("100")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
