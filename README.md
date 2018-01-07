# Общее
Проект содержит [программу для контроля качества данных в таблице БД](https://github.com/alderven/dbchecker/blob/master/dbchecker.py), автотесты и [Allure отчет](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html) с результатами их выполнения.

# Тест-кейсы и результаты выполнения тестов
Отчет Allure: https://rawgit.com/alderven/dbchecker/master/allure-report/index.html

№  | Описание тест-кейса                                           | Тест-скрипт                                                                                                                             | Шаги тест-кейса / Результат прогона
-- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -----------------------------------
1  | Тестирование количества неуникальных комбинаций ID, INT_VALUE | [test_count_of_non_unique_combinations.py](https://github.com/alderven/dbchecker/blob/master/test_count_of_non_unique_combinations.py)  | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/fb0ebcf5e0ec3aee44737dc2b1fbbbd4/a75814101f1e6b48/)
2  | Тестирование среднего значения для параметра "FLOAT_VALUE"    | [test_mean_value_float.py](https://github.com/alderven/dbchecker/blob/master/test_mean_value_float.py)                                  | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/aee3af50da1841e1b6aca21d2eae3a0d/2a98d4ac749471c5/)
3  | Тестирование среднего значения для параметра "INT_VALUE"      | [test_mean_value_int.py](https://github.com/alderven/dbchecker/blob/master/test_mean_value_int.py)                                      | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/3bab18dd969e31449e273264730998a7/62ae0411d33822f6/)
4  | Тестирование NULL значений                                    | [test_null_values.py](https://github.com/alderven/dbchecker/blob/master/test_null_values.py)                                            |  Прошло
4.1| - проверка "ID"                                               | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/748dd49511bff97b57bfa1810d795658/5c529434f3267921/)
4.2| - проверка "LOAD_DATE"                                        | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/748dd49511bff97b57bfa1810d795658/34118901a5d2d06d/)
4.3| - проверка "INT_VALUE"                                        | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/748dd49511bff97b57bfa1810d795658/2f3091c9297a1817/)
4.4| - проверка "FLOAT_VALUE"                                      | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/748dd49511bff97b57bfa1810d795658/9107f5b79c2f84cf/)
4.5| - проверка "CHAR_VALUE"                                       | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/748dd49511bff97b57bfa1810d795658/247e9ff1cbc44738/)
4.6| - проверка "DATE_VALUE"                                       | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/748dd49511bff97b57bfa1810d795658/1a178bea30e5f9ca/)
5  | Тестирование количества записей                               | [test_records_count.py](https://github.com/alderven/dbchecker/blob/master/test_records_count.py)                                        | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/838e81c3dbaedea0d4cad8b6850f50b0/ffd423d98785afcb/)
6  | Тестирование количества 0                                     | [test_zeros_count.py](https://github.com/alderven/dbchecker/blob/master/test_zeros_count.py)                                            |  Прошло
6.1| - проверка "ID"                                               | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/514b5d66295b5fc9c1cb6d6b90d8982c/b65a55f382fad6e7/)
6.2| - проверка "INT_VALUE"                                        | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/514b5d66295b5fc9c1cb6d6b90d8982c/e4db623ed2f6950a/)
6.3| - проверка "FLOAT_VALUE"                                      | -                                                                                                                                       | [Прошло](https://rawgit.com/alderven/dbchecker/master/allure-report/index.html#behaviors/514b5d66295b5fc9c1cb6d6b90d8982c/a17a3774d9ca1d4f/)

# Инсталляция
1. Скачать и распаковать архив с проектом: https://github.com/alderven/dbchecker/archive/master.zip
1. Установить Python 3.6 (и выше): https://www.python.org/downloads/
1. Установить следующие библиотики для Python:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * allure-pytest: https://github.com/allure-framework/allure-pytest
1. Установить Allure Framework: https://docs.qameta.io/allure/latest/

# Как запускать тест:
В командной строке выполнить следующую команду:
```javascript
python -m pytest --alluredir full_path_to_report_folder
```
# Как генерировать Allure отчет:
В командной строке выполнить следующую команду:
```javascript
allure serve full_path_to_report_folder
```
