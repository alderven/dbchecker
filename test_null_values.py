import pytest
import random
from db import DBTest, TABLE_CHECK_OBJECT, current_date
from dbchecker import db_checker

'''
N.B.
Ожидаемое количество NULL при тестировании на NULL параметра "LOAD_DATE" равно 0,
т.к. программа "dbchecker" анализирует данные только за за текущий сутки.
А при "LOAD_DATE" == NULL программа эти даннные не увидит.
'''


@pytest.allure.feature('DBChecker')
@pytest.allure.story('Тестирование NULL значений')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
@pytest.mark.parametrize('parameter_to_check, test_input, expected', [
    ('NULL_ID',          [(None,  current_date(), 0,    random.random(), 'StringA', '2018-01-01')], 1),
    ('NULL_LOAD_DATE',   [(1,     None,           1,    random.random(), 'StringB', '2018-01-02')], 0),
    ('NULL_INT_VALUE',   [(2,     current_date(), None, random.random(), 'StringC', '2018-01-03')], 1),
    ('NULL_FLOAT_VALUE', [(3,     current_date(), 3,    None,            'StringD', '2018-01-04')], 1),
    ('NULL_CHAR_VALUE',  [(4,     current_date(), 4,    random.random(), None,      '2018-01-05')], 1),
    ('NULL_DATE_VALUE',  [(5,     current_date(), 5,    random.random(), 'StringF', None        )], 1),
])
def test_null_values(parameter_to_check, test_input, expected):

    with pytest.allure.step('1. Добавляем данные в таблицу "CHECK_OBJECT": "{}"'.format(test_input)):

        db = DBTest()
        db.insert(TABLE_CHECK_OBJECT, test_input)

    with pytest.allure.step('2. Запускаем программу "checker", она анализирует таблицу "CHECK_OBJECT" '
                            'и сохраняет результат в таблицу "CHECK_STATUS"'):
        db_checker()

    with pytest.allure.step('3. Вычитываем из таблицы "CHECK_STATUS" данные о количестве NULL значений'
                            'для поля: "{}"'.format(parameter_to_check)):

        actual = db.get_value_for(parameter_to_check)
        err_msg = 'Ожидаемое количество NULL значений для поля "{}": {}, количество в таблице "CHECK_OBJECT": {}'.format(parameter_to_check, expected, actual)
        assert actual == expected, err_msg
