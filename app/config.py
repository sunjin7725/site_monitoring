import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

PGSQL_HOST = '121.66.185.30'
PGSQL_PORT = '25432'
PGSQL_DATABASE = 'ba306'
PGSQL_ID = 'kcnet'
PGSQL_PWD = 'kcnet00!@#$'

if os.name == 'nt':
    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '\\data'
    CHROME_DOWNLOAD_DIR = DATA_DIR + '\\driver_download'
else:
    DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/data'
    CHROME_DOWNLOAD_DIR = DATA_DIR + '/driver_download'

date_format_regex = {
    '%Y': "\d{4}",
    '%y': "\d{2}",
    '%m': "\d+",
    '%B': "\w+",
    '%b': "\w{3}",
    '%A': "\w+",
    '%a': "\w{3}",
    '%w': "\d",
    '%d': "\d{2}",
    '%H': "\d{2}",
    '%I': "\d{2}",
    '%M': "\d{2}",
    '%S': "\d{2}",
    '%f': "\d{6}",
    '%p': "\w{2}",
    '%j': "\d{3}",
    '%x': "\d{2}/\d{2}/\d{2}",
    '%X': "\d{2}:\d{2}:\d{2}",
    '%W': "\d{2}",
    '%U': "\d{2}",
}

EC_WAIT = 300
