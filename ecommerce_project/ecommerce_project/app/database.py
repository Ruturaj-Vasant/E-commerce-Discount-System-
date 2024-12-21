from app.logger import logger
import pyodbc
from config import DB_CONFIG

def get_db_connection():
    try:
        conn_str = (
            'DRIVER={ODBC Driver 18 for SQL Server};'
            f'SERVER={DB_CONFIG["server"]};'
            f'DATABASE={DB_CONFIG["database"]};'
            f'UID={DB_CONFIG["username"]};'
            f'PWD={DB_CONFIG["password"]};'
            'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60;'
        )
        connection = pyodbc.connect(conn_str)
        logger.info("Database connection successful")
        return connection
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise
