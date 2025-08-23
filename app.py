from flask import Flask, request, render_template
from config import Configuration
import sqlite3
import os

app = Flask(__name__) 
app.config.from_object(Configuration)

def init_db():  
    with sqlite3.connect('forum.db') as conn:  
        cursor = conn.cursor()  
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                board TEXT NOT NULL, 
                nickname TEXT NOT NULL, 
                content TEXT NOT NULL, 
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                media_path TEXT 
            )
        ''')    
        conn.commit()    
        
        


with app.app_context(): 
    init_db()  

import view