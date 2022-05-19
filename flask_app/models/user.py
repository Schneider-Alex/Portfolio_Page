from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash, session, request
from flask_app import app

class User:
    db = 'portfolio'
    def __init__(self, data): 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']