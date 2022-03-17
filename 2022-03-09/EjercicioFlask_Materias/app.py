import os.path

# sqlarchemy permite conectarse a varias tipos de bases de datos
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect

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
class Subject(db.Model): # clase especial donde va a estar el model de la base de data
    # configuramos las columnas de la base de datos
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.Text)
    approved = db.Column(db.Boolean)


#FUNCIONES CRUD --------------------------------------------------------------------------

def create_subject(name):
    subject = Subject(nom=name)
    db.session.add(subject) # agrega el registro
    db.session.commit() # confirma los cambios
    db.session.refresh(subject)

def read_subjects():
    return db.session.query(Subject).all() #trae todos los elementos de la base de datos


def update_subject(subject_id, name):
    db.session.query(Subject).filter_by(id=subject_id).update({
        "nom": name
    })
    db.session.commit()

def delete_subject(subject_id):
    db.session.query(Subject).filter_by(id=subject_id).delete()
    db.session.commit()


# RUTAS --------------------------------------------------------------------------------------

#
@app.route("/", methods=["POST", "GET"])
def view_index():
    if request.method == "POST":
        create_subject(request.form['nom'])
    return render_template("indexAdmin.html", subjects=read_subjects()) # devuelve-toda el array

#
@app.route("/edit/<subject_id>", methods=["POST", "GET"])
def edit_note(subject_id):
    if request.method == "POST":
        update_subject(subject_id, name=request.form['nom'])
    elif request.method == "GET":
        delete_subject(subject_id)
    return redirect("/", code=302) #luego de editar se vuelve a dirigir a la ruta normal


# cuando se ejecute se crea una instancia de la base de datos y corre el servidor flask
if __name__ == "__main__":
    db.create_all()
    app.run()
