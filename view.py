from flask import render_template, request, redirect, url_for, make_response, send_from_directory, Response
from app import app
import sqlite3
from datetime import datetime
import pytz
import logging
import random
import os
from werkzeug.utils import secure_filename
from flask import send_file


logging.basicConfig(level=logging.DEBUG)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'mp4', 'webm', 'mp3', 'wav', 'flac','aac','alac', 'ogg'}
MAX_FILE_SIZE = 300 * 524 * 524
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    conn = sqlite3.connect('forum.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/download_db")
def download_db():
    try:
        return send_file("forum.db", as_attachment=True)
    except FileNotFoundError:
        return "База не найдена"

@app.route('/static/uploads/<path:filename>')
def serve_uploaded_file(filename):
    mimetype = 'audio/mpeg' if filename.lower().endswith('.mp3') else 'audio/wav' if filename.lower().endswith('.wav') else None
    response = send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype=mimetype, as_attachment=False)
    response.headers['Access-Control-Allow-Origin'] = '*' 
    response.headers['Content-Disposition'] = 'inline' 
    return response

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
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/') 
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  

        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("a", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("a")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("a",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'a'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None  
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("a.html", messages=eest_messages, nickname=nickname)

@app.route("/bo", methods=["GET", "POST"])
def bo():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/')  
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  
        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("bo", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("bo")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("bo",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'bo'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None 
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("bo.html", messages=eest_messages, nickname=nickname)

@app.route("/mus", methods=["GET", "POST"])
def mus():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/')  
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  
        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("mus", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("mus")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("mus",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'mus'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None 
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("mus.html", messages=eest_messages, nickname=nickname)

@app.route("/mov", methods=["GET", "POST"])
def mov():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/')  
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  
        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("mov", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("mov")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("mov",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'mov'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None 
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("mov.html", messages=eest_messages, nickname=nickname)

@app.route("/v", methods=["GET", "POST"])
def v():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)


        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/')  
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  
        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("v", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("v")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("v",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'v'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None 
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("v.html", messages=eest_messages, nickname=nickname)

@app.route("/b", methods=["GET", "POST"])
def b():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/')  
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  
        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("b", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("b")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("b",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'b'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None 
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("b.html", messages=eest_messages, nickname=nickname)

@app.route("/e", methods=["GET", "POST"])
def e():
    conn = get_db_connection()
    nickname = request.cookies.get("nickname", "")
    
    if request.method == "POST":
        content = request.form.get("content")
        form_nickname = request.form.get("nickname")
        file = request.files.get("media")
        media_path = None
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename).replace('\\', '/')  
            file.save(file_path)
            media_path = f"uploads/{unique_filename}"  
        if content and form_nickname:
            conn.cursor().execute(
                "INSERT INTO messages (board, nickname, content, media_path,ip) VALUES (?, ?, ?, ?, ?)",
                ("e", form_nickname, content, media_path, ip)
            )
            conn.commit()
            response = make_response(redirect(url_for("e")))
            response.set_cookie("nickname", form_nickname, max_age=60*60*24*30)
            conn.close()
            return response
        
        conn.close()
    
    messages = conn.cursor().execute(
        "SELECT nickname, content, timestamp, media_path, ip FROM messages WHERE board = ? ORDER BY timestamp DESC",
        ("e",)
    ).fetchall()
    logging.debug(f"{len(messages)} повідомлень для дошки 'e'")
    eest_messages = []
    utc_tz = pytz.timezone("UTC")
    eest_tz = pytz.timezone("Europe/Kiev")
    for msg in messages:
        utc_time = utc_tz.localize(datetime.strptime(msg["timestamp"], "%Y-%m-%d %H:%M:%S"))
        eest_time = utc_time.astimezone(eest_tz).strftime("%Y-%m-%d %H:%M:%S")
        media_path = msg["media_path"].replace('\\', '/') if msg["media_path"] else None 
        eest_messages.append({
            "nickname": msg["nickname"],
            "content": msg["content"],
            "timestamp": eest_time,
            "media_path": media_path,
            "ip": msg["ip"]
        })
    conn.close()
    return render_template("e.html", messages=eest_messages, nickname=nickname)

@app.errorhandler(404)
def page_not_found(e):
    error_images = [
        "images/404_1.jpg",
        "images/404_2.jpg",
        "images/404_3.jpg",
        "images/404_4.jpg",
        "images/404_5.jpg",
        "images/404_6.jpg",
        "images/404_7.jpg",
        "images/404_8.jpg",
        "images/404_9.gif",
        "images/404.png",
        "images/notfound.jpg",
        "images/monkey_not_found.jpg"
    ]
    random_image = random.choice(error_images)
    return render_template("404.html", random_image=random_image), 404
