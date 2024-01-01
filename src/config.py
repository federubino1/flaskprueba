class Config:
    SECRET_KEY = "lwKvZT2w70kRSaOIazTIkbrOFSaJEnnq"

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'inicio_sesion'
    MYSQL_PASSWORD = 'E(chVz9JA2DBsW2/'
    MYSQL_DB = 'users'

config = {
    'development': DevelopmentConfig
}