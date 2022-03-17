import os.path

# sqlarchemy permite conectarse a varias tipos de bases de datos
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect
# from sqlalchemy.orm import relationship

app = Flask (__name__)

# creamos un archivo de tipo de base de datos
dir_folder = os.path.dirname(os.path.abspath(__file__)) # llamamos la url entera para guardarlos en la capeta del proyecto
database_file = "sqlite:///{}".format(os.path.join(dir_folder, "datadb.db"))

# configuracion necesaria
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# llamamos una variable donde la guadamos en la variable db
db = SQLAlchemy(app)

#Modelo de la DB. Con esto ya podemos crear registros
class Game(db.Model): # clase especial donde va a estar el model de la base de data
    # configuramos las columnas de la base de datos
    __tablename__= 'game' # configuramos el nombre de la tabla
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_name = db.Column(db.Text)
    game_platforms = db.Column(db.Text)
    game_release_year = db.Column(db.Text)
    game_description = db.Column(db.Text)
    game_image_link = db.Column(db.Text)
    game_rating = db.Column(db.Text)
    # relacion con la tabla de commentarios
    comments = db.relationship('Comments', backref='game', lazy=True)

#Tabla donde se guardaran los commentarios
class Comments(db.Model):
    # configuramos el nombre de la tabla
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    commentator = db.Column(db.Text)
    comment = db.Column(db.Text)
    # relacion lado a lado con la tabla principal
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=False)


#FUNCIONES CRUD de informacion del juego ---------------------------------------------

#crea un nuevo juego y lo guarda en la base de datos
def create_game(name,platforms,release_year,description,image_link,rating):
    game = Game(game_name=name,game_platforms=platforms,game_release_year=release_year,game_description=description,game_image_link=image_link,game_rating=rating)
    db.session.add(game) # agrega el registro
    db.session.commit() # confirma los cambios
    db.session.refresh(game)

# retorna todos los juegos guardados en la base de datos
def read_games():
    return db.session.query(Game).all() #trae todos los elementos de la base de datos

# actializa la informacion general de un juego
def update_game(id, name,platforms,release_year,description,image_link,rating):
    #como actualizar mas datos -------------------------------------------------------
    db.session.query(Game).filter_by(game_id=id).update({
        "game_name": name,  "game_platforms": platforms, "game_release_year": release_year, "game_description": description, "game_image_link": image_link, "game_rating": rating
    })
    db.session.commit()

# eleimina un juego de la base de datos segun su id
def delete_game(id):
    db.session.query(Game).filter_by(game_id=id).delete()
    db.session.commit()


#FUNCIONES CRUD Para commentarios -----------------------------------------------------

# crea un nuevo comentario
def create_comment(commentator, comment, game_id):
    comment = Comments(commentator=commentator,comment=comment,game_id=game_id)
    db.session.add(comment) # agrega el registro
    db.session.commit() # confirma los cambios
    db.session.refresh(comment)

# retorna todos los comentarios guardados en la base de datos
def read_comment():
    return db.session.query(Comments).all() #trae todos los elementos de la base de datos

# actualiza un comentario de un juego
def update_comment(id, commentator, comment, game_id):
    db.session.query(Comments).filter_by(id=id).update({
        "commentator": commentator, "comment": comment, "game_id": game_id
    })
    db.session.commit()

# eleimina un comentario de un juego
def delete_comment(id):
    db.session.query(Comments).filter_by(id=id).delete()
    db.session.commit()


# RUTAS --------------------------------------------------------------------------------------

# refrezca todos los registros de juegos para pagina de administrador
@app.route("/admin", methods=["POST", "GET"])
def view_indexAdmin():
    if request.method == "POST":
        create_game(request.form['game_name'],request.form['game_platforms'],request.form['game_release_year'],request.form['game_description'],request.form['game_image_link'],request.form['game_rating'])
    return render_template("indexAdmin.html", games=read_games(), comments=read_comment()) # devuelve-toda el array y se la entrega a la vista

# refrezca todos los registros de juegos para la pagina de usuario
@app.route("/", methods=["POST", "GET"])
def view_indexUser():
    if request.method == "POST":
        create_game(request.form['game_name'],request.form['game_platforms'],request.form['game_release_year'],request.form['game_description'],request.form['game_image_link'],request.form['game_rating'])
    return render_template("indexUser.html", games=read_games(), comments=read_comment()) # devuelve-toda el array y se la entrega a la vista

# refrezca todos los comentarios de un juego para la pagina de admin
@app.route("/comments", methods=["POST", "GET"])
def view_indexComments():
    if request.method == "POST":
        create_comment(request.form['commentator'],request.form['comment'],request.form['game_id'])
    return render_template("indexAdmin.html") # devuelve-toda el array

# refrezca todos los registros de comentarios de un juego para la pagina de usuario
@app.route("/commentUser", methods=["POST"])
def view_indexCommentsMain():
    create_comment(request.form['commentator'],request.form['comment'],request.form['game_id'])
    return redirect("/", code=302)

# codigo para actualizar o eliminar algun registro de juego para la vista de admin
@app.route("/edit/<game_id>", methods=["POST", "GET"])
def edit_game(game_id):
    if request.method == "POST":
        update_game(game_id, name=request.form['game_name'], platforms=request.form['game_platforms'], release_year=request.form['game_release_year'], description=request.form['game_description'], image_link=request.form['game_image_link'], rating=request.form['game_rating'])
    elif request.method == "GET":
        delete_game(game_id)
    return redirect("/admin", code=302) #luego de editar se vuelve a dirigir a la ruta normal

# codigo para actualizar o eliminar algun registro de juego para la vista de admin
@app.route("/edit/comments/<id>", methods=["POST", "GET"])
def edit_comment(id):
    if request.method == "POST":
        update_comment(id, commentator=request.form['commentator'], comment=request.form['comment'], game_id=request.form['game_id'])
    elif request.method == "GET":
        delete_comment(id)
    return redirect("/admin", code=302) #luego de editar se vuelve a dirigir a la ruta normal


# cuando se ejecute se crea una instancia de la base de datos y corre el servidor flask
if __name__ == "__main__":
    db.create_all()
    app.run()
