from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "我的第一个网站！部署在 Vercel 啦！"