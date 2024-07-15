from flask import Flask, render_template, jsonify, request, redirect, url_for
import mysql.connector
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/lista')
def list():
    try:
        cursor=db.connection.cursor()
        cursor.execute("select * from db1")
        datos = cursor.fetchall()   
    except Exception as ex:
        print("Something went wrong: {}".format(ex))
        return jsonify({'mensaje':'Error'})
    return render_template('lista.html', datos=datos)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=5001)