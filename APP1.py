"""
[Aplicación básica del microframework Flask de Python]
Author: Fortinux
Date: []
"""
from flask import Flask, render_template
APP1 = Flask(__name__)


@APP1.route("/")
def index():
    return render_template("index.html")


@APP1.route("/servicios")
def servicios():
    return render_template("base.html")


@APP1.route("/contacto")
def contacto():
    return render_template("base.html")


@APP1.route("/admin")
def admin():
    return render_template("base.html")