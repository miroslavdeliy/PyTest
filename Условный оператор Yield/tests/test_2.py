# Импортирование фреймворка
import pytest

# Фиктура
@pytest.fixture
def set_up():
   print("Сообщение перед началом теста")

# 2 псевдотеста без использованием фиктуры
def test_sending_message_1():
   print("Сообщение теста 1")

def test_sending_message_2():
   print("Соощение теста 2")