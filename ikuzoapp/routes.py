from flask import render_template, url_for, redirect, request
from ikuzoapp import app, db
from ikuzoapp.models import *
import secrets, os

@app.route('/')
def bar():
    return render_template('bar.html')
