from db import DB, TABLE_CHECK_OBJECT, TABLE_CHECK_STATUS


class DBChecker(DB):

    @property
    def rows_count(self):
        statement = 'SELECT COUNT(*) FROM {} WHERE LOAD_DATE="{}"'.format(TABLE_CHECK_OBJECT, self.date)
        result = self.query(statement)
        return result.fetchone()[0]

    @property
    def mean_int_value(self):
        statement = 'SELECT AVG(INT_VALUE) FROM {} WHERE LOAD_DATE="{}"'.format(TABLE_CHECK_OBJECT, self.date)
        result = self.query(statement)
        return result.fetchone()[0]

    @property
    def mean_float_value(self):
        statement = 'SELECT AVG(FLOAT_VALUE) FROM {} WHERE LOAD_DATE="{}"'.format(TABLE_CHECK_OBJECT, self.date)
        result = self.query(statement)
        return result.fetchone()[0]

    def get_null_count(self, column_name):
        statement = 'SELECT COUNT(*) FROM {} WHERE {} IS NULL AND LOAD_DATE IS "{}"'.format(TABLE_CHECK_OBJECT,
                                                                                            column_name, self.date)
        result = DB.query(self, statement)
        return result.fetchone()[0]

    @property
    def null_id(self):
        return self.get_null_count('ID')

    @property
    def null_load_date(self):
        return self.get_null_count('LOAD_DATE')

    @property
    def null_int_value(self):
        return self.get_null_count('INT_VALUE')

    @property
    def null_float_value(self):
        return self.get_null_count('FLOAT_VALUE')

    @property
    def null_char_value(self):
        return self.get_null_count('CHAR_VALUE')

    @property
    def null_date_value(self):
        return self.get_null_count('DATE_VALUE')

    def get_zeros_count_for(self, column_name):
        statement = 'SELECT COUNT(*) FROM {} WHERE {} = 0 AND LOAD_DATE IS "{}"'.format(TABLE_CHECK_OBJECT,
                                                                                        column_name, self.date)
        result = DB.query(self, statement)
        return result.fetchone()[0]

    @property
    def zeros_count_id(self):
        return self.get_zeros_count_for('ID')

    @property
    def zeros_count_int(self):
        return self.get_zeros_count_for('INT_VALUE')

    @property
    def zeros_count_float(self):
        return self.get_zeros_count_for('FLOAT_VALUE')

    @property
    def count_of_non_unique_combinations(self):
        statement = 'SELECT ID, INT_VALUE FROM {} WHERE LOAD_DATE="{}"'.format(TABLE_CHECK_OBJECT, self.date)
        result = self.query(statement)
        count = 0
        lst = []
        for row in result:
            item = str(row[0]) + str(row[1])
            if item in lst:
                count += 1
            lst.append(item)
        return count


def db_checker():

    # 1. Инициализируем объект "DBChecker"
    db = DBChecker()

    # 2. Создаем таблицу "CHECK_STATUS"
    columns = '''LOAD_DATE, ROWS_COUNT,
                 NULL_ID, NULL_LOAD_DATE, NULL_INT_VALUE, NULL_FLOAT_VALUE, NULL_CHAR_VALUE, NULL_DATE_VALUE,
                 MEAN_INT_VALUE, MEAN_FLOAT_VALUE,
                 ZERO_ID, ZERO_INT_VALUE, ZERO_FLOAT_VALUE,
                 RECORDS_COUNT_NON_UNIQUE'''
    db.create_table(TABLE_CHECK_STATUS, columns)

    # 3. Подсчитываем данные и добавляем в таблицу "CHECK_STATUS"
    data = [(db.date,
             db.rows_count,
             db.null_id,
             db.null_load_date,
             db.null_int_value,
             db.null_float_value,
             db.null_char_value,
             db.null_date_value,
             db.mean_int_value,
             db.mean_float_value,
             db.zeros_count_id,
             db.zeros_count_int,
             db.zeros_count_float,
             db.count_of_non_unique_combinations)]
    db.insert(TABLE_CHECK_STATUS, data)

    # 4. Закрываем соездинение с БД
    db.close()


if __name__ == '__main__':
    db_checker()
