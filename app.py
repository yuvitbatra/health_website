from flask import Flask, render_template

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'data_management'

@app.route('/')
def Home():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run()