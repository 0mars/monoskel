from uuid import UUID


class Id:
    value: UUID

    def __init__(self, value: UUID):
        self.value = value

    def is_valid(self):
        return len(self.string()) > 0

    def string(self):
        return str(self.value)