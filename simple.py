from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('login.html')

@app.route('/rg/')
def route1():
    return render_template('reg.html')

@app.route('/con')
def con():
   return render_template('contact.html')

@app.route('/ab')
def about():
    return render_template('about.html')

@app.route('/ga')
def gallary():
    return render_template('Gallary.html')

@app.route('/yoga')
def yoga():
    return render_template('yoga.html')
          
if __name__ == '__main__':
    app.run(debug = True)