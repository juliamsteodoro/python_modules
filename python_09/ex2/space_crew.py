from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        if not any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        experienced = sum(
            member.years_experience >= 5 for member in self.crew
        )
        if self.duration_days > 365 and experienced * 2 < len(self.crew):
            raise ValueError(
                "Long missions require at least 50% experienced crew "
                "(5+ years)"
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)
    try:
        commander = CrewMember(
            member_id="CREW-001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=42,
            specialization="Mission Command",
            years_experience=15,
        )
        lieutenant = CrewMember(
            member_id="CREW-002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=8,
        )
        officer = CrewMember(
            member_id="CREW-003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=3,
        )
        mission_data = {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2024-01-01T12:00:00",
            "duration_days": 900,
            "crew": [commander, lieutenant, officer],
            "budget_millions": 2500.0,
        }
        mission = SpaceMission.model_validate(mission_data)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except ValidationError as error:
        print("Validation error:")
        for detail in error.errors():
            print(detail["msg"].removeprefix("Value error, "))
        return

    print("\n" + "=" * 41)
    try:
        SpaceMission.model_validate({
            **mission_data,
            "crew": [lieutenant, officer],
        })
    except ValidationError as error:
        print("Expected validation error:")
        for detail in error.errors():
            print(detail["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
