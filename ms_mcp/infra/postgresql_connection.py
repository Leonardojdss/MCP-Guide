import urllib.parse
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection_uri():

    # Read URI parameters from the environment
    dbhost = os.getenv('DBHOST')
    dbname = os.getenv('DBNAME')
    dbuser = urllib.parse.quote(os.getenv('DBUSER'))
    password = os.getenv('DBPASSWORD')
    sslmode = os.getenv('SSLMODE')
    db_uri = f"host={dbhost} dbname={dbname} user={dbuser} password={password} sslmode={sslmode}"
    # Construct connection URI
    return db_uri