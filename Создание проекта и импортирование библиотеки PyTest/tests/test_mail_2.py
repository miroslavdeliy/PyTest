# Импортирование фреймворка
import pytest

# Фикстура
@pytest.fixture
def set_up():
   print("Вход в систему выполнен")

# 2 Псевдотеста без использования фиктуры
def test_sending_mail_1():
   print("Письмо отправлено")

def test_sending_mail_2():
   print("Письмо отправлено")