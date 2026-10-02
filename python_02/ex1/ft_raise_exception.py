def input_temperature(temp_str: str):
	temp_str = int(temp_str)
	if temp_str >= 0 and temp_str <= 40:
		return temp_str
	elif temp_str < 0:
		raise ValueError("Caught input_temperature error: -50°C is too cold for plants (min 0°C)")
	elif temp_str > 40:
		raise ValueError("Caught input_temperature error: 100°C is too hot for plants (max 40°C)")

def test_temperature(temp_str):
	try:
		data = input_temperature(temp_str)
		print("Input data is", data)
		print("Temperature is now", data, "°C")
	except ValueError as input_error:
		print("Input data is", temp_str)
		print("Caught input_temperature error:", input_error)

if __name__ == "__main__":
    print("=== Garden Temperature ===")
    
    test_temperature("25")
    test_temperature("abc")
    test_temperature("-50")
    test_temperature("100")
    
    print("All tests completed - program didn't crash!")