# models/user.py
class User:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, data):
       # Chuyển đổi key nếu cần
        return User(
            id=data.get("Id") or data.get("id"),
            name=data.get("Name") or data.get("name")
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
