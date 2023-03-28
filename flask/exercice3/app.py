from flask import Flask, render_template, request, redirect, url_for, flash
import mariadb

app = Flask(__name__)
app.secret_key = "mysecretkey"

def get_conn():
    return mariadb.connect(
        host='127.0.0.1',
        port=3306,
        user='etudiant',
        password='123456',
        database='test'
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/membres')
def membres():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS membres (id int NOT NULL AUTO_INCREMENT, pseudo varchar(10) NOT NULL default '', PRIMARY KEY (id));")
    cur.execute("INSERT INTO membres (pseudo) VALUES ('titi'), ('toto'), ('mimi'), ('lulu'), ('nono'), ('roro'), ('jojo'), ('momo'), ('mumu');")
    conn.commit()
    cur.close()
    conn.close()
    flash('Table "membres" créée et données insérées avec succès')
    return redirect(url_for('home'))

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            pseudo = request.form['pseudo']
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM membres WHERE pseudo=%s", (pseudo,))
            result = cur.fetchone()
            if result is not None:
                flash("Le nickname saisi existe déjà")
            else:
                cur.execute("INSERT INTO membres (pseudo) VALUES (%s)", (pseudo,))
                conn.commit()
                flash("Le nouveau nickname a été enregistré")
        except Exception as e:
            flash(str(e))
        finally:
            cur.close()
            conn.close()
    return render_template('form.html')

@app.route('/table')
def table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM membres")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('table.html', membres=data)

if __name__ == '__main__':
    app.run(debug=True)
