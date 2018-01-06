import sqlite3
import datetime

DB_FILE = 'data.db'
TABLE_CHECK_OBJECT = 'CHECK_OBJECT'
TABLE_CHECK_STATUS = 'CHECK_STATUS'


class DB(object):
    def __init__(self):
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

    def query(self, sql):
        result = self.cursor.execute(sql)
        return result

    def create_table(self, table_name, columns):

        # Delete table (if exist)
        try:
            statement = 'DROP TABLE {}'.format(table_name)
            self.query(statement)
        except sqlite3.OperationalError as e:
            print('Unable to delete table "{}". Exception: {}'.format(table_name, e))

        # Create table
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

        columns = '''ID             INTEGER PRIMARY KEY,
                     LOAD_DATE      DATE,
                     INT_VALUE      INTEGER,
                     FLOAT_VALUE    DOUBLE,
                     CHAR_VALUE     CHAR,
                     DATE_VALUE     DATETIME'''
        self.create_table(TABLE_CHECK_OBJECT, columns)

    @property
    def records_count(self):
        statement = 'SELECT ROWS_COUNT FROM {} WHERE LOAD_DATE="{}"'.format(TABLE_CHECK_STATUS, self.date)
        result = DB.query(self, statement)
        return result.fetchone()[0]
