from flask import Flask, render_template,request
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='kamlesh',
                             password='123',
                             db='gehlot',
                             cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)

@app.route("/test")
def login():
    return render_template('data.html')

@app.route('/s',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
     name=request.form['name']
     email=request.form['email']
     try:
  

      with connection.cursor() as cursor:
      
        sql = "INSERT INTO empp (name,email) VALUES (%s, %s)"
        cursor.execute(sql, (name,email))
        connection.commit()
     finally:
      connection.close()
      return "Saved successfully."
    else:
      return "error"
    
if __name__ == "__main__":
    app.run(debug = True)