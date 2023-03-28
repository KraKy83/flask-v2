from flask import Flask
import mariadb

app = Flask(__name__)

conn = mariadb.connect(
	host='127.0.0.1',
	port=3306,
	user='etudiant',
	password='123456',
	database='test')
cur = conn.cursor()

@app.route("/")
@app.route("/index")
def index():
   return "Connected to database test"
   
if __name__ == "__main__":
   app.run()
   
