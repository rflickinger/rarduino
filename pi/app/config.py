import yaml

def load_db_credentials():
    with open('secrets.yml', 'r') as f:
        secrets = yaml.safe_load(f)
    return secrets

class Config:
    secrets = load_db_credentials()
    
    DB_USER = secrets['db_user']
    DB_PASSWORD = secrets['db_password']
    DB_NAME = secrets['db_name']
    DB_HOST = secrets.get('db_host', 'localhost')  # default to localhost

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False