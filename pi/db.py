import psycopg2
import yaml

# Load credentials from secrets.yaml
def load_db_credentials():
    with open('secrets.yml', 'r') as f:
        secrets = yaml.safe_load(f)
    return secrets

def get_connection():
    secrets = load_db_credentials()

    # Get credentials from the secrets.yml
    db_user = secrets['db_user']
    db_password = secrets['db_password']
    db_name = secrets['db_name']
    db_host = "localhost"

    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
    )
    return conn

def init_db(conn):
    print(conn.closed) # 0
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS temperature_log (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMPTZ DEFAULT now(),
                temperature FLOAT NOT NULL
            );
        """)
    conn.commit()

def insert_temp(conn, temp):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO temperature_log (temperature) VALUES (%s);", (temp,))
    conn.commit()