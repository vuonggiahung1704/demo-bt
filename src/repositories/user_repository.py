# repositories/user_repository.py
from config.dynamodb import dynamodb
from constants.table import USER_TABLE
from models.user import User

class UserRepository:
    def __init__(self):
        self.table = dynamodb.Table(USER_TABLE)

    def get(self, user_id):
        print("DEBUG - USER_TABLE:", USER_TABLE)
        print("DEBUG - user_id:", user_id, type(user_id))
        res = self.table.get_item(Key={"Id": user_id})
        item = res.get("Item")
        return User.from_dict(item) if item else None
