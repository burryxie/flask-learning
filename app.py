from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  # return "Hello, Flask!"
  return render_template('index.html')


@app.route("/buss_info")
def buss_info():
  return render_template('buss_info.html')
