import psycopg2

from config import PGSQL_HOST, PGSQL_PORT, PGSQL_DATABASE, PGSQL_ID, PGSQL_PWD

conn = psycopg2.connect(database=PGSQL_DATABASE, user=PGSQL_ID, password=PGSQL_PWD, host=PGSQL_HOST, port=PGSQL_PORT)
