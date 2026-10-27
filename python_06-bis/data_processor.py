from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("Nenhum dado armazenado para extração.")
        item = self._storage.pop(0)
        rank = self._rank_counter
        self._rank_counter += 1
        return (rank, item)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        def _is_valid_log(item: Any) -> bool:
            if not isinstance(item, dict) or len(item) == 0:
                return False
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in item.items()
            )

        if _is_valid_log(data):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(_is_valid_log(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def _format_log(log_dict: dict[str, str]) -> str:
            if "log_level" in log_dict and "log_message" in log_dict:
                return f"{log_dict['log_level']}: {log_dict['log_message']}"
            return ": ".join(log_dict.values())

        if isinstance(data, list):
            for entry in data:
                self._storage.append(_format_log(entry))
        else:
            self._storage.append(_format_log(data))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print("Trying to validate input '42':", num_proc.validate(42))
    print("Trying to validate input 'Hello':", num_proc.validate("Hello"))

    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print("Got exception:", e)

    num_proc.ingest([1, 2, 5 - 7])
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print("Trying to validate input '42':", text_proc.validate(42))
    print("Valid text:", text_proc.validate(["Hello", "Nexus", "World"]))
    text_proc.ingest(["Hello", "Nexus", "World"])
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print("Trying to validate input 'Hello':", log_proc.validate("Hello"))
    print("Valid log:", log_proc.validate({"log_level": "NOTICE"}))
    log_proc.ingest([
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ])
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")
