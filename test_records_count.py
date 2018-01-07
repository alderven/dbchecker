import pytest
import random
from db import DBTest, TABLE_CHECK_OBJECT, current_date, rnd_str
from dbchecker import db_checker


@pytest.allure.feature('DBChecker')
@pytest.allure.story('Тестирование количества записей')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_records_count():

    with pytest.allure.step('1. Добавляем случайное количество записей в таблицу "CHECK_OBJECT"'):

        db = DBTest()
        records_count = random.randint(1, 100)
        data = []
        date = current_date()
        for i in range(records_count):
            row = (i, date, i, random.random(), rnd_str(), date)
            data.append(row)
        db.insert(TABLE_CHECK_OBJECT, data)

    with pytest.allure.step('2. Запускаем программу "checker", она анализирует таблицу "CHECK_OBJECT" '
                            'и сохраняет результат в таблицу "CHECK_STATUS"'):
        db_checker()

    with pytest.allure.step('3. Вычитываем из таблицы "CHECK_STATUS" данные о количестве записей, '
                            'сравниваем с ожидаемым значением: {}'.format(records_count)):

        err_msg = 'Ожидаемое количество записей: {}, количество записей в таблице "CHECK_OBJECT": {}'.format(records_count, db.records_count)
        assert records_count == db.records_count, err_msg
