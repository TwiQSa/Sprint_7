import allure
import requests
from test_data import *

class TestCourierLogin:
    @allure.title('Проверки: 1.Курьер может авторизоваться. 2.Для авторизации нужно передать все обязательные поля 3.Успешный запрос возвращает id')
    def test_courier_login(self):
        payload = {
            "login": "Tester1",
            "password": "123456",
        }

        re = requests.post(COURIER_LOGIN_URL, json=payload)
        assert re.status_code == 200
        assert "id" in re.json()

    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать пароль')
    def test_courier_login_wrong_password(self):
        payload = {
            "login": "Tester1",
            "password": "123457",
        }

        re = requests.post(COURIER_LOGIN_URL, json=payload)
        assert re.status_code == 404
        assert re.json() == {"code": 404,"message": "Учетная запись не найдена"}

    @allure.title('Проверки: 1.Система вернёт ошибку, если неправильно указать логин 2.Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_courier_login_wrong_login(self):
        payload = {
            "login": "Test222",
            "password": "123456",
        }

        re = requests.post(COURIER_LOGIN_URL, json=payload)
        assert re.status_code == 404
        assert re.json() == {"code": 404,"message": "Учетная запись не найдена"}

    @allure.title('Проверка, если какого-то поля нет, запрос возвращает ошибку')
    def test_courier_login_missing_field(self):
        payload = {
            "password": "1234"
        }

        re = requests.post(COURIER_LOGIN_URL, json=payload)
        assert re.status_code == 400
        assert re.json() == {"code": 400,"message": "Недостаточно данных для входа"}