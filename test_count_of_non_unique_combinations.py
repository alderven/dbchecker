import sys
import pytest
import random
from db import DBTest, TABLE_CHECK_OBJECT, current_date, rnd_str
from dbchecker import db_checker


@pytest.allure.feature('DBChecker')
@pytest.allure.story('Тестирование количества неуникальных комбинаций ID, INT_VALUE')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_count_of_non_unique_combinations_count():

    with pytest.allure.step('1. Добавляем случайное количество записей в таблицу "CHECK_OBJECT"'):

        db = DBTest()
        data = []
        date = current_date()

        with pytest.allure.step('1.1 Добавляем записи с уникальной комбинацией ID, INT_VALUE'):

            records_count_unique = random.randint(1, 100)
            for i in range(records_count_unique):
                row = (random.randint(0, sys.maxsize), date, random.randint(0, sys.maxsize), random.random(), rnd_str(), date)
                data.append(row)

        with pytest.allure.step('1.1 Добавляем записи с неуникальной комбинацией ID, INT_VALUE'):

            records_count_non_unique = random.randint(2, 100)
            for i in range(records_count_non_unique):
                non_unique_id = random.randint(0, sys.maxsize)
                non_unique_int_value = random.randint(0, sys.maxsize)
                row_1 = (non_unique_id, date, non_unique_int_value, random.random(), rnd_str(), date)
                row_2 = (non_unique_id, date, non_unique_int_value, random.random(), rnd_str(), date)
                data.extend([row_1, row_2])

        db.insert(TABLE_CHECK_OBJECT, data)

    with pytest.allure.step('2. Запускаем программу "checker", она анализирует таблицу "CHECK_OBJECT" '
                            'и сохраняет результат в таблицу "CHECK_STATUS"'):
        db_checker()

    with pytest.allure.step('3. Вычитываем из таблицы "CHECK_STATUS" данные о количестве неуникальных комбинаций '
                            'ID, INT_VALUE, сравниваем с ожидаемым значением: {}'.format(records_count_non_unique)):

        err_msg = 'Ожидаемое количество записей: {}, количество записей в таблице "CHECK_OBJECT": {}'.format(records_count_non_unique, db.records_count_non_unique)
        assert records_count_non_unique == db.records_count_non_unique, err_msg
