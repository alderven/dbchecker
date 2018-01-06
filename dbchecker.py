from db import DB, TABLE_CHECK_OBJECT, TABLE_CHECK_STATUS


class DBChecker(DB):

    @property
    def rows_count(self):
        statement = 'SELECT COUNT(*) FROM {} WHERE LOAD_DATE="{}"'.format(TABLE_CHECK_OBJECT, self.date)
        result = self.query(statement)
        return result.fetchone()[0]


def db_checker():

    # 1. Initialize DB instance
    db = DBChecker()

    # 2. Create "CHECK_STATUS" table
    columns = 'LOAD_DATE, ROWS_COUNT'
    db.create_table(TABLE_CHECK_STATUS, columns)

    # 3. Calculate data and insert it into "CHECK_STATUS" table
    data = [(db.date, db.rows_count)]
    db.insert(TABLE_CHECK_STATUS, data)

    # 4. Close connection to DB
    db.close()


if __name__ == '__main__':
    db_checker()
