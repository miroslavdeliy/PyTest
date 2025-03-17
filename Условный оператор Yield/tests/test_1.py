# Импортирование фреймворка
import pytest

# Фиктура
@pytest.fixture
def set_up():
   print("Сообщение перед началом теста")
   yield
   print('Сообщение после выполнения теста')

# 2 псевдотеста с использованием фиктуры
def test_sending_message_1(set_up):
   print("Сообщение теста 1")

def test_sending_message_2(set_up):
   print("Соощение теста 2")