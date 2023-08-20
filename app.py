# app.py

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017/")  # MongoDB 서버 주소
db = client["myblog"]  # 데이터베이스 이름
collection = db["posts"]  # 컬렉션 이름

@app.route("/")
def index():
    # 게시글 목록을 가져옴
    posts = list(collection.find())
    return render_template("index.html", posts=posts)

@app.route("/asdf.html")
def asdf():
    # 게시글 목록을 가져옴
    posts = list(collection.find())
    return render_template("asdf.html", posts=posts)

@app.route("/add_post", methods=["POST"])
def add_post():
    # 게시글 추가
    title = request.form["title"]
    content = request.form["content"]
    post = {"title": title, "content": content}
    collection.insert_one(post)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
