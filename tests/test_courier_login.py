import requests

class TestCourierLogin:
    #Проверки: 1.курьер может авторизоваться. 2.для авторизации нужно передать все обязательные поля 3.успешный запрос возвращает id
    def test_courier_login(self):
        payload = {
            "login": "Tester1",
            "password": "123456",
        }

        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=payload)
        assert re.status_code == 200
        assert "id" in re.json()

    #система вернёт ошибку, если неправильно указать пароль
    def test_courier_login_wrong_password(self):
        payload = {
            "login": "Tester1",
            "password": "123457",
        }

        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=payload)
        assert re.status_code == 404
        assert re.json() == {"code": 404,"message": "Учетная запись не найдена"}

    #Проверки: 1. система вернёт ошибку, если неправильно указать логин 2. если авторизоваться под несуществующим пользователем, запрос возвращает ошибку
    def test_courier_login_wrong_login(self):
        payload = {
            "login": "Test222",
            "password": "123456",
        }

        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=payload)
        assert re.status_code == 404
        assert re.json() == {"code": 404,"message": "Учетная запись не найдена"}

    #если какого-то поля нет, запрос возвращает ошибку
    def test_courier_login_missing_field(self):
        payload = {
            "password": "1234"
        }

        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login", json=payload)
        assert re.status_code == 400
        assert re.json() == {"code": 400,"message": "Недостаточно данных для входа"}