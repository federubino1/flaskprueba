from models.entities.User import User

class ModelUser():
    def login(db, user):
        try:    
            cursor = db.connection.cursor()
            sql = "SELECT email, user, password FROM users WHERE user = %s AND email = %s"
            cursor.execute(sql, (user.username, user.email))
            row = cursor.fetchone()
            
            if row != None:
                user = User(row[0],row[1],User.checkPassword(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)