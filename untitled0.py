import pymysql 
from flask import Flask ,render_template,request
 
db=pymysql.connect(host="localhost",user="kamlesh",password="123",database="gehlot")

cursol=db.cursor()

app = Flask(__name__)

pymysql = pymysql(app)

@app.route ('/','GET','POST')
def home():
    if request.method=='POST':
                
        userDetails=request.form
        userDetails = request.form
        First_Name = userDetails['Last_Name']
        Last_Name = userDetails['Last_Name']
        Mobile  = userDetails['Mobile']
        EMail = userDetails['EMail']
        Password  = userDetails['Password']
        Confrom_Password = userDetails['Confrom_Password']
        Sex = userDetails['Sex']
        
        cursol.execute("insert into Register values (%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))
        pymysql.connection.commit()
        cursol.close()
        return render_template('reg.html')
        



