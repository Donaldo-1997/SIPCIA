'''
    importo el framework flask que me ayudara a trabajar en el aplicativo,
    junto me traigo las clases tambien.

    *lineas de codigo para instalar el flask*
    pip install flask

    *linea de codigo para instalar mysql*
    pip install Flask-MySQLdb
'''

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#importo la clase de configuracion creada
from config import config

#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.Users import Users

from routes.users import *

#instancio la clase flask
app = Flask(__name__)

#declaro variable para llamar al metodo MySQL pasandole el parametro de app el cual contiene la clase instanciada de flask
db = MySQL(app)

#creo ruta principal utilizando el decorador @ que me redirige al login
@app.route('/')

#defino una funcion para redireccionar la pagina a esa ruta establecida
def index():
    return redirect(url_for('login'))
    

#creo ruta principal utilizando el decorador @ y le asigno los metodos a recibir porque por defecto recibe metodo GET
@app.route('/login', methods = ["GET", "POST"])
#defino una funcion para redireccionar la pagina a esa ruta establecida
# def login():
#     logged_user = 0
#     if request.method == 'POST':
#         user = Users(0, 0, 0, 0, 0, 0, request.form['user'], request.form['password'], 0)
#         logged_user = ModelUser.login(db,user)
    
#     if logged_user > 0:
#         return render_template("home.html")
#     else:
#         flash("user not found") 
#         return render_template("login.html")

#creo nueva utilizando el decorador @
@app.route('/home')

#defino una funcion para redireccionar la pagina a esa ruta establecida
def home():
    return render_template("home.html")

#validacion para ejecutar el servidor y que este en constante movimiento
if __name__ == '__main__':
    #utilizo la configuracion del diccionario config en su llave development
    app.config.from_object(config['development'])
    app.run()