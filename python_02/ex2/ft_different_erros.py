def garden_operations(operation_number):
	if operation_number == 0:
		int("abc")
	elif operation_number == 1:
		result = 10 / 0
	elif operation_number == 2:
		f = open("taylorswift.txt", "r")
		print(f.read())
	elif operation_number == 3:
		var = 5 + "texto"

def test_error_types():
	for i in range(5):
		try:
			garden_operations(i)
		except ValueError as bad_data:
			print(f"Caught ValueError: {bad_data}")
		except ZeroDivisionError as divided_zero:
			print(f"Caught ZeroDivisionError: {divided_zero}")
		except TypeError as type_error:
			print(f"Caught TypeError: {type_error}")
		except FileNotFoundError as notfound_file:
			print(f"FileNotFoundError {notfound_file}")
			