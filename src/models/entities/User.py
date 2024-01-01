from werkzeug.security import check_password_hash

class User():
    def __init__(self, email, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password
    
    @classmethod
    def checkPassword(self, password_hash, password):
        return (check_password_hash(password_hash, password))