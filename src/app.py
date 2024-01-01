from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import config
from flask_mysqldb import MySQL

# Modelos:
from models.ModelUser import ModelUser

# Entidades:
from models.entities.User import User

class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(config['development'])
        self.db = MySQL(self.app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/')(self.index)
        self.app.route('/login', methods=['GET', 'POST'])(self.login)
        self.app.route('/home')(self.home)

    def run(self):
        self.app.run()

    def index(self):
        return redirect(url_for('login'))

    def login(self):
        if "user" in session:
            return redirect(url_for('home'))
        if request.method == 'POST':
            user = User(request.form['email'].lower(), request.form['username'], request.form['password'])
            logged_user = ModelUser.login(self.db, user)

            if logged_user is not None:
                if logged_user.password:
                    session["user"] = request.form['username']
                    return redirect(url_for('home'))
                else:
                    flash('Contraseña no válida')
            else:
                flash('Usuario no encontrado...')
                return render_template('auth/login.html')
        else:
            return render_template('auth/login.html')

    def home(self):
        return render_template('home.html')

if __name__ == "__main__":
    my_app = MyApp()
    my_app.run()