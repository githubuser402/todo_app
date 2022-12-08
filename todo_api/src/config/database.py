from pathlib import Path

DATABASE_URL = f'sqlite://{Path(__name__).parent}/db.sqlite3'