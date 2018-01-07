import pytest
import random
from db import DBTest, TABLE_CHECK_OBJECT, current_date
from dbchecker import db_checker


@pytest.allure.feature('DBChecker')
@pytest.allure.story('Тестирование количества 0')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
@pytest.mark.parametrize('parameter_to_check, test_input, expected', [
    ('ZERO_ID',          [(0, current_date(), 1,    random.random(), 'StringA', '2018-01-01')], 1),
    ('ZERO_INT_VALUE',   [(1, current_date(), 0,    random.random(), 'StringC', '2018-01-02')], 1),
    ('ZERO_FLOAT_VALUE', [(2, current_date(), 3,    0,               'StringD', '2018-01-03')], 1),
])
def test_zeros_count(parameter_to_check, test_input, expected):

    with pytest.allure.step('1. Добавляем данные в таблицу "CHECK_OBJECT": "{}"'.format(test_input)):

        db = DBTest()
        db.insert(TABLE_CHECK_OBJECT, test_input)

    with pytest.allure.step('2. Запускаем программу "checker", она анализирует таблицу "CHECK_OBJECT" '
                            'и сохраняет результат в таблицу "CHECK_STATUS"'):
        db_checker()

    with pytest.allure.step('3. Вычитываем из таблицы "CHECK_STATUS" данные о количестве 0 '
                            'для поля: "{}"'.format(parameter_to_check)):

        actual = db.get_value_for(parameter_to_check)
        err_msg = 'Ожидаемое количество 0 для поля "{}": {}, количество в таблице "CHECK_OBJECT": {}'.format(parameter_to_check, expected, actual)
        assert actual == expected, err_msg
