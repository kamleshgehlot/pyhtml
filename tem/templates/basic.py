from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])



def basic():
   
    if request.method == 'POST':
        if request.form['name'] and request.form['pass']:
            return 'Validation successful'
        else:
            return 'Validation unsuccessful'
        return 'Hi'
    
    
         
    return render_template('def.html')
        

if __name__ == '__main__':
    app.run()