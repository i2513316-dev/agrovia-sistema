import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "gateway01.ap-northeast-1.prod.aws.tidbcloud.com"),
        port=int(os.getenv("DB_PORT", "4000")),
        database=os.getenv("DB_NAME", "2tjdWwLxpawErDb.root"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD" 2NZoG1v6MzN2rflu""),
        ssl_disabled=os.getenv("DB_SSL", "true").lower() != "true",
    )


def query(sql, params=(), one=False):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(sql, params)
        rows = cur.fetchone() if one else cur.fetchall()
        return rows
    finally:
        cur.close()
        conn.close()

def execute(sql, params=()):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        conn.commit()
        return cur.lastrowid
    finally:
        cur.close()
        conn.close()
