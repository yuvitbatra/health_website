import time

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'data_management'

@app.route('/')
def loader():
    return render_template('loader.html')

@app.route('/HomePage')
def HomePage():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()