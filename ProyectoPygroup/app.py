import os.path

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


database_file = "sqlite:///database/data.db"

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


def login_teacher(cod):
    students = Student.query.all()
    teacher = Teacher.query.filter_by(cod=cod).first()
    subject = Subject.query.filter_by(id=int(teacher.id_subject)).first()
    grades = Grades.query.filter_by(id_subject=int(teacher.id_subject)).all()
    print(subject)
    return render_template("indexTeacher.html", students=students, teacher=teacher, grades=grades, subject=subject)


def login_estudiante(cod):
    student = Student.query.filter_by(cod=int(cod)).first()
    subjects = Subject.query.all()
    grades = Grades.query.filter_by(cod_student=int(cod)).all()
    print(grades)
    print(subjects)
    return render_template("indexStudent.html", student=student, subjects=subjects, grades=grades)


@app.route('/cancelar/<id>/<cod>')
def delete(id,cod):
    grade=Grades.query.filter_by(id=int(id)).delete()
    db.session.commit()
    student = Student.query.filter_by(cod=int(cod)).first()
    url = ('http://127.0.0.1:5000/login?co=' + cod + '&pass=' + student.password)
    return redirect(url)

@app.route('/login', methods=["GET"])
def login():
    student = Student.query.filter_by(cod=request.args["co"], password=request.args["pass"]).first()
    if (student != None):
        return login_estudiante(student.cod)
    else:
        teacher = Teacher.query.filter_by(cod=request.args["co"], password=request.args["pass"]).first()
        if (teacher != None):
            return login_teacher(teacher.cod)
    return "Codigo o contraseña erroneos"


@app.route('/login/estudiante/<cod>/<id>', methods=["POST","GET"])
def inscription(cod,id):
    grades = Grades(id_subject=int(id),cod_student=int(cod),grade=0)
    student = Student.query.filter_by(cod=cod).first()
    db.session.add(grades)
    db.session.commit()
    url = ('http://127.0.0.1:5000/login?co=' + cod + '&pass=' + student.password)
    return redirect(url)


@app.route('/login/nueva', methods=["GET","POST"])
def get_grade(x):
    return request.args.get(x)


@app.route('/login/nota/<cod>/<codT>', methods=["GET","POST"])
def change_grades(cod,codT):
    teacher = Teacher.query.filter_by(cod=codT).first()
    grade = Grades.query.filter_by(id_subject=int(teacher.id_subject),cod_student=int(cod)).first()
    grade.grade = get_grade("nota")
    if(int(grade.grade)>=0 and int(grade.grade)<=5):
        db.session.commit()
        url = ('http://127.0.0.1:5000/login?co=' + codT + '&pass=' + teacher.password)
        return redirect(url)
    return "Ingrese una nota entre 0 y 5"


@app.route('/estudiante', methods=["POST"])
def add_student():
    student=Student(cod=request.form["codS"],name=request.form["nameS"],password=request.form["passwordS"])
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/profesor/materia', methods=["GET","POST"])
def validate_subject(subj):
    subject = Subject.query.filter_by(name=subj).first()
    if subject != None:
        return subject.id
    return None


@app.route('/profesor', methods=["POST"])
def add_teacher():
    subj=validate_subject(request.form["subject"])
    if subj != None:
        teacher = Teacher(cod=request.form["codT"], name=request.form["nameT"], password=request.form["passwordT"],id_subject=subj)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('home'))
    return "Esa materia no existe"


@app.route('/materia',methods=["POST"])
def add_subject():
    subject = Subject(name=request.form["sub"])
    db.session.add(subject)
    db.session.commit()
    return redirect(url_for('home'))


class Student (db.Model):
    cod = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    grades = db.relationship('Grades', backref='student', lazy=True)


class Subject (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    grades = db.relationship('Grades', backref='subject', lazy=True)
    teacher = db.relationship('Teacher', backref='subject', lazy=True)


class Grades (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_subject = db.Column(db.Integer, db.ForeignKey('subject.id'),nullable=False)
    cod_student = db.Column(db.Integer, db.ForeignKey('student.cod'),nullable=False)
    grade = db.Column(db.Integer)


class Teacher (db.Model):
    cod = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    id_subject = db.Column(db.Integer, db.ForeignKey('subject.id'),nullable=False)


@app.route('/')
def home():
    return render_template("index.html")

# Init
if __name__ == "__main__":
    app.run(debug=True)