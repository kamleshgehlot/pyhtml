import pymysql
from flask import Flask, request
from DBUtils.PersistentDB import PersistentDB    

app = Flask(__name__)    

def connect_db():
    return PersistentDB(
        creator = pymysql,
        user = 'kamlesh', password = '123', database = 'gehlot', 
        autocommit = True, charset = 'utf8mb4', 
        cursorclass = pymysql.cursors.DictCursor)

def get_db():
    if not hasattr(app, 'db'):
        app.db = connect_db()
    return app.db.connection()    

@app.route('/')
def hello_world():
    city = request.args.get('city')

    cursor = get_db().cursor()
    cursor.execute('SELECT city_id FROM city WHERE city = %s', city)
    row = cursor.fetchone()

    if row:
      return 'City "{}" is #{:d}'.format(city, row['city_id'])
    else:
      return 'City "{}" not found'.format(city)