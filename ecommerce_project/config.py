DB_CONFIG = {
    'server': 'trade-server-dev.database.windows.net',
    'database': 'InternationalTradeDB',
    'username': 'CloudSA119c44c1',
    'password': 'NewSecurePassword@123'
}

SQLALCHEMY_DATABASE_URI = (
    'mssql+pyodbc://CloudSA119c44c1:NewSecurePassword@123@'
    'trade-server-dev.database.windows.net:1433/InternationalTradeDB'
    '?driver=ODBC+Driver+18+for+SQL+Server'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
