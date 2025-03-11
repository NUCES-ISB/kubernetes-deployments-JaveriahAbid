from flask import Flask
import psycopg2
import os

app = Flask(__name__)

db_host = os.getenv("POSTGRES_HOST", "localhost")
db_name = os.getenv("POSTGRES_DB", "postgres")
db_user = os.getenv("POSTGRES_USER", "admin")
db_pass = os.getenv("POSTGRES_PASSWORD", "password")

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_pass,
            host=db_host
        )
        conn.close()
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

db_host = os.getenv("POSTGRES_HOST", "localhost")
db_name = os.getenv("POSTGRES_DB", "postgres")
db_user = os.getenv("POSTGRES_USER", "admin")
db_pass = os.getenv("POSTGRES_PASSWORD", "password")

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_pass,
            host=db_host
        )
        conn.close()
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    