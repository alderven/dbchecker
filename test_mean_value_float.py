import pytest
import random
from db import DBTest, TABLE_CHECK_OBJECT, current_date, rnd_str
from dbchecker import db_checker


@pytest.allure.feature('DBChecker')
@pytest.allure.story('Тестирование среднего значения для параметра "FLOAT_VALUE"')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
def test_mean_value_float():

    with pytest.allure.step('1. Добавляем случайное количество записей в таблицу "CHECK_OBJECT"'):

        db = DBTest()
        records_count = random.randint(2, 100)
        data = []
        date = current_date()
        floats_sum = 0
        for i in range(records_count):
            float_value = random.random()
            floats_sum += float_value
            row = (i, date, i, float_value, rnd_str(), date)
            data.append(row)
        db.insert(TABLE_CHECK_OBJECT, data)
        expected = str(floats_sum / records_count)[:10]  # выставляем точность в 10 цифр

    with pytest.allure.step('2. Запускаем программу "checker", она анализирует таблицу "CHECK_OBJECT" '
                            'и сохраняет результат в таблицу "CHECK_STATUS"'):
        db_checker()

    with pytest.allure.step('3. Вычитываем из таблицы "CHECK_STATUS" данные о среднем значении параметра "FLOAT_VALUE", '
                            'сравниваем с ожидаемым значением: {}'.format(expected)):

        actual = str(db.mean_float)[:10]  # выставляем точность в 10 цифр
        err_msg = 'Ожидаемое среднее значение параметра "FLOAT_VALUE": {}, среднее значение из таблицы "CHECK_OBJECT": {}'.format(expected, actual)
        assert expected == actual, err_msg
