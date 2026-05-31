from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    grade = request.form['grade']
    major = request.form['major']

    with open('responses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, grade, major])

    return "Response Saved!"


if __name__ == '__main__':
    app.run(debug=True)