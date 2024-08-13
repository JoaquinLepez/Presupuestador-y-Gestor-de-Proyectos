from werkzeug.security import generate_password_hash, check_password_hash

class Security:

    @staticmethod
    def generate_password(password: str) -> str:
        return generate_password_hash(password)
    
    @staticmethod
    def check_password(hashed_password: str, plain_password: str) -> bool:
        return check_password_hash(hashed_password, plain_password)
