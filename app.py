from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():
    if request.method == 'POST':
        return "Welcome %s!" % request.form['username']
