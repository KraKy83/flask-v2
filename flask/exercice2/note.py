from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('form_note'))

@app.route('/form-note', methods=['GET', 'POST'])
def form_note():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_grade = float(request.form['student_grade'])
        return redirect(url_for('note_score', student_name=student_name, student_grade=student_grade))
    return render_template('form-note.html')

@app.route('/note-score/<student_name>/<float:student_grade>')
def note_score(student_name, student_grade):
    if student_grade >= 10.0:
        message = f"Bonjour {student_name}, vous avez la moyenne !"
    else:
        message = f"Bonjour {student_name}, vous n'avez pas la moyenne !"
    return render_template('note-score.html', message=message)

@app.route('/grading-info')
def grading_info():
    return render_template('grading.html')

if __name__ == '__main__':
    app.run(debug=True)
