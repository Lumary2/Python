from flask import Flask, render_template
import names

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():

  return names.name()

if __name__ == '__main__':
  app.run(debug=True)





