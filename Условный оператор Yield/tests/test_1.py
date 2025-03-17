import pytest

# Фикстура возвращает список
@pytest.fixture
def data():
    test_list = [1, 2, 3, 4, 5]
    print(f'Тестовый список {test_list}')
    yield test_list
    print('Расчет выполнен')


# Расчет суммы списка из фикстуры
def test_sum(data):
    print(f'Сумма списка: {sum(data)}')


# Расчет среднего списка из фикстуры
def test_average(data):
    print(f'Среднее списка: {sum(data)/len(data)}')