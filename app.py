from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def start():
    return "heloOOO"

@app.route("/mbsa")
def mbsa():
    return render_template('D:\d\check\check1\index.html')

