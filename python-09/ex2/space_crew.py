from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Rank(str, Enum):
	CADET = "cadet"
	OFFICER = "officer"
	LIEUTENANT = "lieutenant"
	CAPTAIN = "captain"


class CrewMember(BaseModel):
	member_id: str = Field(min_length=3, max_length=10)
	name: str = Field(min_length=2, max_length=50)
	rank: Rank
	age: int = Field(ge=18, le=80)
	years_of_experience: int = Field(ge=0)
	specialization: str = Field(min_length=3, max_length=50)

	@model_validator(mode="after")
    def validate_crew_member(self) -> "CrewMember":
        if not self.member_id.startswith("CREW-"):
            raise ValueError("O ID do tripulante deve começar com 'CREW-'")
        return self


class SpaceMission(BaseModel):
	mission_id: str = Field(min_length=5, max_length=15)
	mission_name: str = Field(min_length=3, max_length=100)
	destination: str = Field(min_length=3, max_length=50)
	launch_date: datetime
	duration_days: int = Field(ge=1, le=3650)
	crew: List[CrewMember]
	mission_status: str = Field(default="planned")
	budget_millions: float = Field(ge=1, le=10000.0)

	@model_validator(mode='after')
	def validate_mission_rules(self) -> 'SpaceMission':
		if not self.mission_id.startswith("MIS-"):
			raise ValueError("")
		if self.duration_days > 365
			has_captain = any(member.rank == Rank.CAPTAIN for member in self.crew)
			experienced_count = sum(1 for member in self.crew if member.years_of_experience >= 5)
			experienced_ratio = experienced_count / len(self.crew)
			if not has_captain and experienced_ratio < 0.5:
				raise ValueError("")
		return self


def main() -> None:
    print("=== Validação de Tripulação e Missão Espacial ===")
    captain = CrewMember(
        member_id="CREW-001",
        name="Sarah Connor",
        rank=Rank.CAPTAIN,
        age=42,
        years_of_experience=15,
        specialization="Command",
    )
    officer = CrewMember(
        member_id="CREW-002",
        name="John Glenn",
        rank=Rank.OFFICER,
        age=28,
        years_of_experience=3,
        specialization="Navigation",
    )

    try:
        valid_mission = SpaceMission(
            mission_id="MIS-2026-01",
            mission_name="Exploração de Marte",
            destination="Marte",
            launch_date=datetime.now(),
            duration_days=500,
            crew=[captain, officer],
            budget_millions=1500.0,
        )
        print("✅ Missão válida criada com sucesso:")
        print(
            f"Missão: {valid_mission.mission_name} | Tripulantes: {len(valid_mission.crew)}"
        )
    except ValidationError as e:
        print("Erro inesperado:", e)

    print("======================================")
    try:
        cadet1 = CrewMember(
            member_id="CREW-003",
            name="Novato 1",
            rank=Rank.CADET,
            age=22,
            years_of_experience=1,
            specialization="Engineering",
        )
        cadet2 = CrewMember(
            member_id="CREW-004",
            name="Novato 2",
            rank=Rank.CADET,
            age=23,
            years_of_experience=1,
            specialization="Biology",
        )
        invalid_mission = SpaceMission(
            mission_id="MIS-2026-02",
            mission_name="Viagem Sem Experiência",
            destination="Júpiter",
            launch_date=datetime.now(),
            duration_days=600,
            crew=[cadet1, cadet2],
            budget_millions=2000.0,
        )
    except ValidationError as e:
        print("⚠️ Erro de validação esperado capturado com sucesso:")
        print(e)


if __name__ == "__main__":
    main()