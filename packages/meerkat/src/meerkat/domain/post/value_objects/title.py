class Title:
    value: str

    def __init__(self, value):
        self.value = value

    def is_valid(self):
        return len(self.value) > 0

    def __str__(self):
        return self.value
