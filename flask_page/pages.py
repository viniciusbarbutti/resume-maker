from flask import Flask, render_template, request
from wtforms import StringField, Form, SubmitField
from app.auxiliar import mount_json
from app.make import create

page = Flask(__name__)


class Cadastro(Form):
    name = StringField('Name')
    function = StringField('Function')
    phone = StringField('Phone')
    email = StringField('Email')
    address = StringField('Address')
    education = StringField('Education')
    experience = StringField('Experience')
    skills = StringField('Skills')
    languages = StringField('Languages')
    but = SubmitField('Send!')


@page.route('/', methods=['GET'])
def index():
    return 'Welcome to resume maker'


@page.route('/make', methods=['GET', 'POST'])
def make():
    if request.method == 'GET':
        return render_template('make.html', form=Cadastro())

    else:
        return mount_json(Cadastro(request.form))


@page.route('/themes', methods=['GET'])
def themes():
    pass


def start_flask():
    page.run()
