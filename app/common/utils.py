import os
import re
import psycopg2
import psycopg2.extras as extras

from datetime import datetime
from common.custom_logger import logger
from common.db_connection import conn

from config import date_format_regex


def regex_number(text):
    return re.sub('[^\d+]', '', text)


def date_change(date, date_format):
    try:
        date = datetime.strptime(date, date_format).strftime("%Y%m%d")
    except:
        try:
            date = date_regex(date, date_format)
            date = datetime.strptime(date, date_format).strftime("%Y%m%d")
        except Exception as e:
            pass
    return date


def date_regex(date, date_format):
    compiler = date_format
    for key, value in date_format_regex.items():
        compiler = compiler.replace(key, value)
    return re.search(compiler, date, re.MULTILINE).group()


def chrome_close(driver):
    try:
        driver.close()
        driver.quit()
    except:
        pass


def to_sql(df, table, _conn=conn):
    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))

    query = "INSERT INTO %s(%s) VALUES %%s ON CONFLICT ON CONSTRAINT %s DO NOTHING" % (table, cols, table + '_pkey')
    cursor = _conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        _conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(f"[Error]::{table}/{len(df)} insert error occurred by {error}")
        _conn.rollback()
        cursor.close()
        raise error
    cursor.close()