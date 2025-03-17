import pytest

@pytest.fixture(scope='module')
def message_module():
    print("Это демонстрационная работа фикстуры модуля.")
    yield
    print("Здесь фиктура модуля уничтожается")


# Фикстура возвращает список работает внутри функции
@pytest.fixture(scope='function')
def data():
    test_list = [1, 2, 3, 4, 5]
    print(f'Тестовый список {test_list}')
    yield test_list
    print('Расчет выполнен')


