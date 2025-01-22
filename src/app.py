from flask import Flask, render_template, redirect, url_for, flash, request
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
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM empleados;"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    return render_template('index.html', empleados = data)


@app.route('/add_empleado', methods=['POST'])
def add_empleado():
    nombre = request.form['nombre']
    apellido1 = request.form['apellido1']
    apellido2 = request.form['apellido2']
    departamento = request.form['departamento']
    salario = request.form['salario']

    if nombre and apellido1 and apellido2 and departamento and salario:
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO empleados (nombre, apellido1, apellido2, departamento, salario) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nombre, apellido1, apellido2, departamento, salario)) 
        mysql.connection.commit()

        return redirect(url_for('home'))
    
    return redirect(url_for('home'))


@app.route('/delete_empleado/<string:id>')
def delete_empleado(id):
    cursor = mysql.connection.cursor()
    sql = "DELETE FROM empleados WHERE id = %s;"
    cursor.execute(sql, (id,))
    mysql.connection.commit()

    return redirect(url_for('home'))


@app.route('/edit_empleado/<string:id>')
def edit_empleado(id):
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM empleados WHERE id = %s"
    cursor.execute(sql, (id,))
    data = cursor.fetchall()

    return render_template('edit_empleado.html', empleado = data)


@app.route('/actualizar_empleado/<string:id>', methods=['POST'])
def actualizar_empleado(id):
    nombre = request.form['nombre']
    apellido1 = request.form['apellido1']
    apellido2 = request.form['apellido2']
    departamento = request.form['departamento']
    salario = request.form['salario']

    cursor = mysql.connection.cursor()
    sql = "UPDATE empleados SET nombre = %s, apellido1 = %s, apellido2 = %s, departamento = %s, salario = %s WHERE id = %s;"
    cursor.execute(sql, (nombre, apellido1, apellido2, departamento, salario, id,))
    mysql.connection.commit()

    return redirect(url_for('home'))
    



if __name__ == '__main__':
    app.config.from_object(['development'])
    app.run()