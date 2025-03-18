import pytest

# Расчет суммы списка из фикстуры
@pytest.mark.run(order=2)
def test_sum(data):
    print(f'Сумма списка: {sum(data)}')


# Расчет среднего списка из фикстуры
@pytest.mark.run(order=3)
def test_average(data):
    print(f'Среднее списка: {sum(data)/len(data)}')


# Разворачивание списка
@pytest.mark.run(order=6)
def test_reverse(data):
    print(f'Развернутый список {reversed(data)}')


# Поиск максимального элемента списка
@pytest.mark.run(order=4)
def test_max_value(data):
    print(f'Максимальный элемент списка {max(data)}')


# Поиск минимального элемента в списке
@pytest.mark.run(order=5)
def test_min_value(data):
    print(f'Минимальный элемент списка {min(data)}')


# Расчет длины списка
@pytest.mark.run(order=1)
def test_len_list(data):
    print(f'Длина списка {len(data)}')