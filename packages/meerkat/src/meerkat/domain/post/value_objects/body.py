from dataclasses import dataclass


@dataclass(frozen=True)
class Body:
    value: str

    def is_valid(self):
        return len(self.value) > 0

    def __str__(self):
        return self.value
