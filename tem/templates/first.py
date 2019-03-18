from flask import Flask, render_template, request, redirect
import pymysql
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
db = pymysql.connect(host="localhost", user="kamlesh", passwd="123", database="gehlot")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        First_Name = userDetails['Last_Name']
        Last_Name = userDetails['Last_Name']
        Mobile  = userDetails['Mobile']
        EMail = userDetails['EMail']
        Password  = userDetails['Password']
        Confrom_Password = userDetails['Confrom_Password']
        Sex = userDetails['Sex'] 
        cur = pymysql.connection.cursor()
        cur.execute("insert into Register values (%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))
        pymysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = pymysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)