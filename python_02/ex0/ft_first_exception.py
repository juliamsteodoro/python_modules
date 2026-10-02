def input_temperature(temp_str: str):
	data = int(temp_str)
	return data

def test_temperature(data):
	try:
		input_temperature(data)
		print("Input data is", data)
		print("Temperature is now", data, "°C")
	except ValueError as input_error:
		print("Input data is", data)
		print("Caught input_temperature error:", input_error)
	
if __name__ == "__main__":
    print("=== Garden Temperature ===")
    
    test_temperature(25)
    
    test_temperature("abc")
    
    print("All tests completed - program didn't crash!")
