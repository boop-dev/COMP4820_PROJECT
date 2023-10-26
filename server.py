# from pylint import epylint

from flask import Flask, render_template
# from subprocess import PIPE, STDOUT, run

app = Flask(__name__)
current_user = None


@app.route('/', methods=['GET', 'POST'])
def login():
    """Starting page of the server, login.html"""
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


def main():
    app.run()

main()