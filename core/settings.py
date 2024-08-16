from configparser import ConfigParser

CONFIG = ConfigParser
CONFIG.read('config.ini')

TOKEN = CONFIG.get('telegram','TOKEN')



PGHOST = CONFIG.get('database', 'PGHOST')
PGDATABASE = CONFIG.get('database', 'PGDATABASE')
PGUSER = CONFIG.get('database', 'PGUSER')
PGPASSWORD = CONFIG.get('database', 'PGPASSWORD')
PGPORT = CONFIG.get('database', 'PGPORT')