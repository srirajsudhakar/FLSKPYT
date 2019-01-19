from flask import Flask,render_template
from data import Faculties
app=Flask(__name__)
Myfaculty=Faculties()
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('Login.html')
@app.route('/register')
def register():
    return render_template('Register.html')
@app.route('/faculty')
def Faculty():
    return render_template('Faculty.html',f = Myfaculty)
if (__name__ == "__main__"):
   app.run(debug=True)
