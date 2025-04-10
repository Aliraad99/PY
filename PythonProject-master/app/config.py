import os
from dotenv import load_dotenv 

load_dotenv()

MSSQL_USERNAME = os.getenv("MSSQL_USERNAME")
MSSQL_PASSWORD = os.getenv("MSSQL_PASSWORD")
MSSQL_SERVER = os.getenv("MSSQL_SERVER")
MSSQL_DATABASE = os.getenv("MSSQL_DATABASE")

DATABASE_URL = f"mssql+aioodbc://{MSSQL_USERNAME}:{MSSQL_PASSWORD}@{MSSQL_SERVER}/{MSSQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
