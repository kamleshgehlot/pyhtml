from flask import Flask, render_template,request,session,redirect,url_for
import pymysql.cursors

pymysql.install_as_MySQLdb()

app = Flask(__name__)

connection = pymysql.connect(host='localhost',
                             user='kamlesh',
                             password='123',
                             db='gehlot',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userDetails = request.form
       
        cursor = connection.cursor()
        try:
            First_Name = userDetails.get('First_Name')
            Last_Name = userDetails.get('Last_Name')
            Mobile  = userDetails.get('Mobile')
            EMail = userDetails.get('EMail')
            Password  = userDetails.get('Password')
            Confrom_Password = userDetails.get('Confrom_Password')
            Sex = userDetails.get('Sex') 
            
            cursor = connection.cursor()
                     
            cursor.execute("INSERT INTO register(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex) VALUES (%s,%s,%s,%s,%s,%s,%s)",(First_Name,Last_Name,Mobile,EMail,Password,Confrom_Password,Sex))
            
            connection.commit()
            return redirect('/log')

        except:
                        
            
            return redirect(url_for('/con'))
            connection.rollback()
            
    else:
      
      return render_template("reg.html")
      cursor.close()
    
    

@app.route('/login',methods=["GET","POST"])
def login(): 
    if request.method == 'POST':
        
        
        EMail = request.form['EMail']
        Password = request.form['Password']
        
        print("helloooooooooooo")
        #cursor = connection.cursor()
        curl = connection.cursor(pymysql.cursors.DictCursor)
        curl.execute("SELECT * FROM  register WHERE EMail=%s ",(EMail))
      
        user = curl.fetchone()
        curl.close()
        
        
        if len(user) > 0:
            
            if ((Password, user['Password']) or user['Password'] or (EMail, user['EMail']) or user['EMail']) :
               
                session['EMail'] = request.form ['EMail']
                session['Password'] = request.form['Password']
               
                return redirect("/yoga")
            else:
                print("hello")
                return "Error password and email not match"
        else:
            print("pyhton")
            return "Error user not found"
    else:
        print("hey")
        return render_template('login.html')
        
   
@app.route('/yoga')
def signup():
    return render_template('yoga.html')

@app.route('/log')
def route():       
    return render_template('login.html')

@app.route('/reg')
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

if __name__ == '__main__':
    
    app.secret_key = 'SAd12b15@5%&154 '
    app.run(debug=True)