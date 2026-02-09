import os  
import time
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=os.environ.get('DB_HOST'),      
                database=os.environ.get('DB_NAME'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD')
            )
            return conn
        except psycopg2.OperationalError:
            print("Baza de date nu e gata, mai incerc in 2 secunde...")
            time.sleep(2)

@app.route('/')
def hello():

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visits (count INT)')
    cur.execute('SELECT count FROM visits')
    result = cur.fetchone()
    
    if result is None:
        cur.execute('INSERT INTO visits (count) VALUES (1)')
        count = 1
    else:
        count = result[0] + 1
        cur.execute('UPDATE visits SET count = %s', (count,))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return f"Salut! Pagina asta a lui Robert a fost vizitata de {count} ori.\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)