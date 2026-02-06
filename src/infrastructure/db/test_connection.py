import psycopg2
from infrastructure.db.config import DATABASE_URL

def test_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        cursor.execute("SELECT 1;")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        print("✅ Conexión exitosa a PostgreSQL:", result)

    except Exception as e:
        print("❌ Error de conexión:", e)

if __name__ == "__main__":
    test_db_connection()