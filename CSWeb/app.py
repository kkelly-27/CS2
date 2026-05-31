from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/submit', methods=['GET'])
def submit():

    name = request.args.get('name')
    grade = request.args.get('grade')
    major = request.args.get('major')

    with open('responses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, grade, major])

    return """
    <h2>Response Saved!</h2>
    <a href="/">Back to Survey</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
