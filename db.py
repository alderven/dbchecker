import sqlite3
import datetime
import random
import string

DB_FILE = 'data.db'
TABLE_CHECK_OBJECT = 'CHECK_OBJECT'
TABLE_CHECK_STATUS = 'CHECK_STATUS'


class DB(object):
    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()
        self.date = current_date()

    def query(self, sql):
        result = self.cursor.execute(sql)
        return result

    def create_table(self, table_name, columns):

        # Удаляем таблицу (если существует)
        try:
            statement = 'DROP TABLE {}'.format(table_name)
            self.query(statement)
        except sqlite3.OperationalError as e:
            print('Unable to delete table "{}". Exception: {}'.format(table_name, e))

        # Создаем таблицу
        statement = 'CREATE TABLE {} ({})'.format(table_name, columns)
        self.query(statement)

    def insert(self, table_name, data):
        lst = len(data[0]) * '?'
        values = ','.join(lst)
        statement = 'INSERT INTO {} VALUES ({})'.format(table_name, values)
        self.cursor.executemany(statement, data)
        self.connection.commit()

    def close(self):
        self.connection.close()


class DBTest(DB):

    def __init__(self):
        super().__init__()  # overwrite parent "init"

        columns = '''ID             INTEGER,
                     LOAD_DATE      DATE,
                     INT_VALUE      INTEGER,
                     FLOAT_VALUE    DOUBLE,
                     CHAR_VALUE     CHAR,
                     DATE_VALUE     DATETIME'''
        self.create_table(TABLE_CHECK_OBJECT, columns)

    @property
    def records_count(self):
        return self.get_value_for('ROWS_COUNT')

    @property
    def mean_int(self):
        return self.get_value_for('MEAN_INT_VALUE')

    @property
    def mean_float(self):
        return self.get_value_for('MEAN_FLOAT_VALUE')

    @property
    def records_count_non_unique(self):
        return self.get_value_for('RECORDS_COUNT_NON_UNIQUE')

    def get_value_for(self, column_name):
        statement = 'SELECT {} FROM {} WHERE LOAD_DATE="{}"'.format(column_name, TABLE_CHECK_STATUS, self.date)
        result = DB.query(self, statement)
        return result.fetchone()[0]


def current_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def rnd_str():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
