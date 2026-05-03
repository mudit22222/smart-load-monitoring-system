import sqlite3

DB_NAME = "energy_data.db"

def init_db():
    """Create the database and table if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_logs (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            voltage   REAL NOT NULL,
            current   REAL NOT NULL,
            power     REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized.")

def insert_data(voltage, current, power):
    """Insert a new energy reading into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO energy_logs (voltage, current, power) VALUES (?, ?, ?)",
        (voltage, current, power)
    )
    conn.commit()
    conn.close()

def fetch_all():
    """Fetch all stored readings (optional utility)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM energy_logs ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
