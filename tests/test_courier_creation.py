import requests

class TestCourierCreation:
    #Проверки: 1. Курьера можно создать. 2.Чтобы создать курьера, нужно передать в ручку все обязательные поля. 3.запрос возвращает правильный код ответа. 4.успешный запрос возвращает {"ok":true}
    def test_create_courier(self):
        payload = {
            "login": "Tester2024",
            "password": "123456",
            "firstName": "Courierb2"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    #Проверка, если одного из полей нет, запрос возвращает ошибку
    def test_create_courier_missing_password_field(self):
        payload = {
            "login": "Tester18922",
            "firstName": "Courierb2"
        }

        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload)

        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    #Проверка, что нельзя создать двух одинаковых курьеров
    def test_create_two_identical_couriers(self):
        payload = {
            "login": "Tester561",
            "password": "123456",
            "firstName": "Courierb2"
        }

        r = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload)
        assert r.status_code == 201
        assert r.json() == {"ok": True}
        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload)
        assert re.status_code == 409
        assert re.json() == {"code": 409,"message": "Этот логин уже используется. Попробуйте другой."}

    #Проверка, если создать пользователя с логином, который уже есть, возвращается ошибка
    def test_create_courier_with_repeating_login(self):
        payload = {
            "login": "Tester1",
            "password": "123456",
            "firstName": "Courierb2"
        }

        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", json=payload)
        assert re.status_code == 409
        assert re.json() == {"code": 409,"message": "Этот логин уже используется. Попробуйте другой."}


