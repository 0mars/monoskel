from uuid import UUID


class Id:
    value: UUID

    def __init__(self, value: UUID):
        self.value = value

    def is_valid(self):
        return len(str(self)) > 0

    def __str__(self):
        return str(self.value)
