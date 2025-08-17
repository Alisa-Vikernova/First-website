from flask import render_template, request, redirect, url_for, make_response
from app import app
import sqlite3
from datetime import datetime
import pytz
import logging
import random

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_db_connection():
    conn = sqlite3.connect('forum.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/a", methods=["GET", "POST"])
def a():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("a", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("a")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("a",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'a'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("a.html", messages=eest_messages, nickname=nickname)

@app.route("/bo", methods=["GET", "POST"])
def bo():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("bo", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("bo")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("bo",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'bo'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("bo.html", messages=eest_messages, nickname=nickname)

@app.route("/mus", methods=["GET", "POST"])
def mus():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("mus", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("mus")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("mus",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'mus'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("mus.html", messages=eest_messages, nickname=nickname)



@app.route("/mov", methods=["GET", "POST"])
def mov():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("mov", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("mov")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("mov",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'mov'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("mov.html", messages=eest_messages, nickname=nickname)

@app.route("/v", methods=["GET", "POST"])
def v():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("v", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("v")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("v",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'v'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("v.html", messages=eest_messages, nickname=nickname)

@app.route("/b", methods=["GET", "POST"])
def b():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("b", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("b")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("b",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'b'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("b.html", messages=eest_messages, nickname=nickname)

@app.route("/e", methods=["GET", "POST"])
def e():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        
        if content and form_nickname:
            conn.cursor().execute("INSERT INTO messages (board, nickname, content) VALUES (?, ?, ?)", ("e", form_nickname, content))
            conn.commit()
            response = make_response(redirect(url_for("e")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute("SELECT nickname, content, timestamp FROM messages WHERE board = ? ORDER BY timestamp DESC", ("e",)).fetchall()
    logging.debug(f"{len(messages)} messages for board 'e'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        eest_messages.append({"nickname": msg["nickname"], "content": msg["content"], "timestamp": eest_time})
    conn.close()
    return render_template("e.html", messages=eest_messages, nickname=nickname)

@app.errorhandler(404)
def page_not_found(e):
    error_images = [
        "images/404_2.jpg",
        "images/404_3.jpg",
        "images/404_4.jpg",
        "images/404_5.jpg",
        "images/404_8.jpg",
        "images/404_9.gif",
        "images/404.png"
    ]
    # Вибираємо випадкову картинку
    random_image = random.choice(error_images)
    return render_template("404.html", random_image=random_image), 404