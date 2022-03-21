import os.path

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

dir_folder = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(dir_folder, "datadb.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Modelo de la DB
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.Text)
    approved = db.Column(db.Boolean)


# Funciones CRUD
def create_subject(name):
    subject = Subject(nom=name)
    db.session.add(subject)
    db.session.commit()
    db.session.refresh(subject)


def read_subjects():
    return db.session.query(Subject).all()


def update_subject(subject_id, name):
    db.session.query(Subject).filter_by(id=subject_id).update({
        "nom": name
    })
    db.session.commit()


def delete_subject(subject_id):
    db.session.query(Subject).filter_by(id=subject_id).delete()
    db.session.commit()


# Rutas
@app.route("/", methods=["POST", "GET"])
def view_index():
    if request.method == "POST":
        create_subject(request.form['nom'])
    return render_template("index.html", subjects=read_subjects())


@app.route("/edit/<subject_id>", methods=["POST", "GET"])
def edit_note(subject_id):
    if request.method == "POST":
        update_subject(subject_id, name=request.form['nom'])
    elif request.method == "GET":
        delete_subject(subject_id)
    return redirect("/", code=302)


# Init
if __name__ == "__main__":
    db.create_all()
    app.run()