from flask import Flask

app = Flask(__name__)
app.debug = True

#@app.route('/')
def hello_world():
   return "Hello : Bonjour tout le monde!"

app.add_url_rule('/hello','hello',hello_world)

if __name__ == '__main__':
   app.run()
   
