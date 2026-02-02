# controllers/user_controller.py
from services.user_service import UserService
from repositories.user_repository import UserRepository
from shared.response import success, error


import logging

def lambda_handler(event, context):
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Received event: {event}")
    path_params = event.get("pathParameters")
    if not path_params or "id" not in path_params:
        logging.error("Missing pathParameters or id in event")
        return error("Missing pathParameters or id", 400)

    user_id = path_params["id"]
    service = UserService(UserRepository())
    try:
        user = service.get_user(user_id)
        logging.info(f"User found: {user}")
        return success(user.to_dict())
    except Exception as e:
        logging.error(f"Error: {e}")
        return error(str(e))
