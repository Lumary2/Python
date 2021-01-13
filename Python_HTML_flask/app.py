from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/students'

db=SQLAlchemy(app)

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))
  pet=db.Column(db.String(40))

  def __init__(self,fname,lname,pet):
    self.fname=fname
    self.lname=lname
    self.pet=pet


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  fname= request.form['fname']
  lname=request.form['lname']
  pet=request.form['pets']

  student=Student(fname,lname,pet)
  db.session.add(student)
  db.session.commit()

  #fetch a certain student2
  studentResult=db.session.query(Student).filter(Student.id==1)
  for result in studentResult:
    print(result.fname)

  return render_template('success.html', data=fname)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)





