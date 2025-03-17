# Расчет суммы списка из фикстуры
def test_sum(message_module, data):
    print(f'Сумма списка: {sum(data)}')


# Расчет среднего списка из фикстуры
def test_average(message_module, data):
    print(f'Среднее списка: {sum(data)/len(data)}')