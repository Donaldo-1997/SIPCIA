#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.Users import Users

#defino una funcion para redireccionar la pagina a esa ruta establecida
def login():
    logged_user = 0
    if request.method == 'POST':
        user = Users(0, 0, 0, 0, 0, 0, request.form['user'], request.form['password'], 0)
        logged_user = ModelUser.login(db,user)
    
    if logged_user > 0:
        return render_template("home.html")
    else:
        flash("user not found") 
        return render_template("login.html")