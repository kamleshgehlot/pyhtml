from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('first.html', name = user)

@app.route('/yoga/<user>')
def yoga(user):
    return render_template('yoga.html', name = user)

@app.route('/gallary/<user>')
def gallary(user):
    return render_template('Gallary.html', name = user)

@app.route('/about/<user>')
def about(user):
    return render_template('about.html', name = user)

@app.route('/reg/<user>')
def reg(user):
    return render_template('reg.html', name = user)

@app.route('/contact/<user>')
def con(user):
    return render_template('contact.html', name = user)
  

if __name__ == '__main__':
    app.run(debug = True)