from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType (str, Enum):
	RADIO = "radio"
	VISUAL = "visual"
	PHYSICAL = "physical"
	TELEPATHIC = "telepathic"

class AlienContact(BaseModel):
	contact_id: str = Field(min_length=5, max_length=15)
	timestamp: datetime
	location: str = Field(min_length=3, max_length=100)
	contact_type: ContactType
	signal_strength: float = Field(ge=0.0, le=10.0)
	duration_minutes: int = Field(ge=1, le=1440)
	witness_count: int = Field(ge=1, le=100)
	message_received: Optional[str] = Field(default=None, max_length=500)
	is_verified: bool = Field(default=False)

	@model_validator(mode='after')
	def validate_contact_rules(self) -> 'AlienContact':
		if not self.contact_id.startswith("AC-")
			raise ValueError("O ID do contato deve começar com 'AC-'")
		if self.contact_type in [ContactType.PHYSICAL, ContactType.ABDUCTION] and not self.is_verified:
			raise ValueError("")
		if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
			raise ValueError("")
		if signal_strength > 7.0 and not self.message_received:
			raise ValueError("")
	

def main() -> None:
	print("Alien Contact Log Validation")
	print("======================================")
	try:
		valid_contact = AlienContact(
            contact_id="AC-2024-001",
            timestamp=datetime.now(),
            location="Área 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Saudações de Zeta Reticuli",
            is_verified=True,)
		print("Contato válido criado com sucesso:")
		print()
	except ValidationError as e:
		print(f"Erro: {e}")
	print("======================================")
	try:
		invalid_contact = AlienContact(
            contact_id="AC-2024-002",
            timestamp=datetime.now(),
            location="Montanha do Diabo",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=False)
	except ValidationError as e:
		print(f"Error: {e}")

if __name__ == "__main__":
    main()