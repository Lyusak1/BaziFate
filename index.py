from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    return "你们好呀！这是Lewis的第一个网站！"
