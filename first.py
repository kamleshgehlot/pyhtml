from flask import Flask, render_template,request,redirect, session
import pymysql.cursors
import bcrypt

connection = pymysql.connect(host='localhost',
                             user='kamlesh',
                             password='123',
                             db='gehlot',
                             cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)

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
        cur = pymysql.connection.cursor()
        cur.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))
        pymysql.connection.commit()
        cur.close()
        return redirect('/user')
    return render_template('reg.html')
  
@app.route('/user')
def users():
    cur = pymysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM register")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html',userDetails=userDetails)
    
    
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        
        EMail = request.form['EMail']
        Password = request.form['Password'].encode('utf-8')

        curl = pymysql.connection.cursor(pymysql.cursors.DictCursor)
        curl.execute("SELECT * FROM  register WHERE EMail=%s , Password=%s",(EMail,Password))
        user = curl.fetchone()
        curl.close()

        if len(user) > 0:
            if bcrypt.hashpw(Password, user["Password"].encode('utf-8')) == user["Password"].encode('utf-8'):
                session['EMail'] = user['EMail']
                session['Password'] = user['Password']
                return render_template('yoga.html')
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")
        
if __name__ == '__main__':
    app.run(debug=True)