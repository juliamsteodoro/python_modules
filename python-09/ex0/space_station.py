from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime

class SpaceStation(BaseModel):
	station_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=1, max_length=50)
	crew_size: int = Field(ge=1, le=20)
	power_level: float = Field(ge=0.0, le=100.0)
	oxygen_level: float = Field(ge=0.0, le=100.0)
	last_maintenance: datetime
	is_operational: bool = True
	notes: Optional[str] = Field(default=None, max_length=500)

def main() -> None:
	print("Space Station Validation")
	print("=" * 40)
	try:
		station = SpaceStation(
			station_id="ISS001",
			name="Estação Espacial Internacional",
			crew_size=6,
			power_level=85.5,
			oxygen_level=92.3,
			last_maintenance=datetime.now(),
			notes="All good"
		)
		print("Valid station report:")
		print(f"ID: {station.station_id}")
		print(f"Name: {station.name}")
		print(f"Crew size: {station.crew_size}")
		print(f"Power level: {station.power_level}%")
		print(f"Oxygen level: {station.oxygen_level}%")
		print(f"Last maintenance: {station.last_maintenance:%Y-%m-%d %H:%M:%S}")
		print(f"Operational: {'Yes' if station.is_operational else 'No'}")
		print(f"Notes: {station.notes}")
	except ValidationError as e:
		print("Validation error:")
		for error in e.errors():
			print(f"{error['loc'][0]}: {error['msg']}")
	print()
	print("=" * 40)
	try:
		invalid_station = SpaceStation(
			station_id="ISS002",
			name="Julia-Stellaris",
			crew_size=50,
			power_level=85.5,
			oxygen_level=92.3,
			last_maintenance=datetime.now()
		)
		print(invalid_station)
	except ValidationError as e:
		print("Expected validation error:")
		for error in e.errors():
			print(f"{error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
	main()
