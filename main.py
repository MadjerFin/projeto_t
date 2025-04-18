from flask import Flask, render_template, request, Response
from duvidas import bot

app = Flask(__name__)
app.secret_key = 'TRIP'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods = ['POST'])
def chat():
    prompt = request.json['msg']
    resposta = bot(prompt)
    return resposta


if __name__=="__main__":
    app.run(debug = True)