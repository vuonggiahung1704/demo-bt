from constants.error_code import USER_NOT_FOUND

class UserService:
    def __init__(self, repo):
        self.repo = repo

    def get_user(self, user_id):
        user = self.repo.get(user_id)
        if not user:
            raise Exception(USER_NOT_FOUND)
        return user
