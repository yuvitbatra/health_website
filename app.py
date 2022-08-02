from flask import Flask, render_template, redirect, session

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'data_management'

@app.route('/')
def HomePage():
    return render_template('layout.html')