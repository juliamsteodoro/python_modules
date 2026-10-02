class GardenError(Exception):
	def __init__(self, message="Unknown plant error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message="Unknown plant error"):
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message="Unknown water error"):
		super(). __init__(message)

def test():
	raise PlantError("")