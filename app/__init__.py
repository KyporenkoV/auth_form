from flask import render_template, Flask, url_for, session,redirect,request, abort,flash
import os


# DATABASE = 'tmp/flsite.db'
DEBUG = True
SECRET_KEY = '12345678'


pwdApp = Flask(__name__)
pwdApp.config.from_object(__name__)

# app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

from app import routes
from app import forms

