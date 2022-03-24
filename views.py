from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, url_for


cart = Blueprint("cart", __name__, url_prefix="/cart")
categories = Blueprint("categories", __name__, url_prefix="/categories")

RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}

# @cart.route("/", methods=["GET"])
# def show_product():
#     create_zone('Centro')
#     return render_template('cart.html')
#
# @categories.route("/", methods=["GET"])
# def show_categories():
#     return render_template('categories.html')


# Rutas
# @app.route("/", methods=["POST", "GET"])
# def view_index():
#     if request.method == "POST":
#         create_subject(request.form['nom'])
#     return render_template("index.html", subjects=read_subjects())
#
#
# @app.route("/edit/<subject_id>", methods=["POST", "GET"])
# def edit_note(subject_id):
#     if request.method == "POST":
#         update_subject(subject_id, name=request.form['nom'])
#     elif request.method == "GET":
#         delete_subject(subject_id)
#     return redirect("/", code=302)