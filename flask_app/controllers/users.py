from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')