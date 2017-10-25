# Author:	Salaheldin Akl
# Student Num:	D15124122
#
# Date: 25.10.2017

from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'toor'
app.config['MYSQL_DB'] = 'tasklist'
app.config['MYSQL_HOST'] = '35.195.113.122'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/list")
def list_tasks(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM tasks''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/add/<task>")
def add_task(task):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tasks (task) VALUES (\'" + task + "\');")
    cur.execute("commit;")
    return "Added"

@app.route("/delete/<task>")
def del_task(task):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE task=\'" + task + "\';")
    cur.execute("commit;")
    return "Deleted"

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
