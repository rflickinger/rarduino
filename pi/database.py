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

def insert_sensor_data(sensor, value):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO sensor_data (sensor, value) VALUES (%s, %s)", (sensor, value))

def get_latest_sensor_data(sensor):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT value, timestamp FROM sensor_data
                WHERE sensor = %s
                ORDER BY timestamp DESC LIMIT 1
            """, (sensor,))
            row = cur.fetchone()
            return {"value": row[0], "timestamp": row[1]} if row else None
