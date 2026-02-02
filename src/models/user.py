# models/user.py
class User:
    def __init__(self, pk: str, name: str):
        self.pk = pk
        self.name = name

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            "pk": self.pk,
            "name": self.name
        }
