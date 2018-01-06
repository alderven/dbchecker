import pytest
import random
import datetime
import string
from db import DBTest, TABLE_CHECK_OBJECT
from dbchecker import db_checker


@pytest.allure.feature('DBChecker')
@pytest.allure.story('Тестирование количества записей')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_dbchecker_records_count():

    with pytest.allure.step('1. Добавляем несколько записей в таблицу "CHECK_OBJECT"'):

        db = DBTest()
        records_count = random.randint(1, 10)
        data = []
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        for i in range(records_count):
            rnd_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            row = (i, date, i, random.random(), rnd_str, date)
            data.append(row)
        db.insert(TABLE_CHECK_OBJECT, data)

    with pytest.allure.step('2. Запускаем программу "checker", она анализирует таблицу "CHECK_OBJECT" '
                            'и сохраняет результат в таблицу "CHECK_STATUS"'):
        db_checker()

    with pytest.allure.step('3. Вычитываем из таблицы "CHECK_STATUS" данные о количестве записей, '
                            'сравниваем с ожидаемым значением: {}'.format(records_count)):

        err_msg = 'Ожидаемое количество записей: {}, количество записей из таблицы "CHECK_OBJECT": {}'.format(records_count, db.records_count)
        assert records_count == db.records_count, err_msg
