import requests
import pytest

class TestOrderCreation:
    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order(self, color):
        order_data = {
            "firstName": "Вадим",
            "lastName": "Ярославов",
            "address": "Пушкина 12",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-08-08",
            "comment": "Требуется срочная доставка",
            "color": color
        }

        re = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/orders", json=order_data)

        assert re.status_code == 201
        assert "track" in re.json()