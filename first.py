from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)


db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['localhost:5000']
app.config['MYSQL_USER'] = db["kamlesh"]
app.config['MYSQL_PASSWORD'] = db["123"]
app.config['MYSQL_DB'] = db["gehlot"]

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        userDetails = request.form
        First_Name = userDetails['Last_Name']
        Last_Name = userDetails['Last_Name']
        Mobile  = userDetails['Mobile']
        EMail = userDetails['EMail']
        Password  = userDetails['Password']
        Confrom_Password = userDetails['Confrom_Password']
        Sex = userDetails['Sex'] 
        cur = mysql.connection.cursor()
        cur.execute("insert into Register values (%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))
        mysql.connection.commit()
        cur.close()
        return redirect('/user')
    return render_template('index.html')

@app.route('/user')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Register")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)