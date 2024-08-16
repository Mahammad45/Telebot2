import psycopg2

from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read('config.ini')

TOKEN = CONFIG.get('telegram','TOKEN')



PGHOST = CONFIG.get('database', 'PGHOST')
PGDATABASE = CONFIG.get('database', 'PGDATABASE')
PGUSER = CONFIG.get('database', 'PGUSER')
PGPASSWORD = CONFIG.get('database', 'PGPASSWORD')
PGPORT = CONFIG.get('database', 'PGPORT')


PGCONN = psycopg2.connect(
    host=PGHOST,
    database=PGDATABASE,
    user=PGUSER,
    password=PGPASSWORD,
    port=PGPORT
)

