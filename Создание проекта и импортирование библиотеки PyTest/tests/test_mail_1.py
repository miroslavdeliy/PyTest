# Импортирование фреймворка
import pytest

# Фиктура
@pytest.fixture
def set_up():
   print("Вход в систему выполнен")

# 2 псевдотеста с использованием фиктуры
def test_sending_mail_1(set_up):
   print("Письмо отправлено")

def test_sending_mail_2(set_up):
   print("Письмо отправлено")