import datetime
import geocoder
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'data_management'

#using geocoder to get user location
g = geocoder.ip('me')
location = g.latlng

@app.route('/')
def HomePage():
    return render_template('layout.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
@app.route('/location')
def address():
    return render_template('hospitals.html')

if __name__ == '__main__':
    app.run()