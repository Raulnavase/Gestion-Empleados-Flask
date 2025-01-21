from flask import Flask, render_template, redirect, url_for, flash
from config import config
from dotenv import load_dotenv
from os import getenv
from flask_mysqldb import MySQL

load_dotenv()

app = Flask(__name__)


app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = getenv('MYSQL_DB')
app.secret_key = getenv('SECRET_KEY')

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')







if __name__ == '__main__':
    app.config.from_object(['development'])
    app.run()