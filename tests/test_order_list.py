import requests

class TestOrderList:
    def test_get_order_list(self):
        re = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders")

        assert re.status_code == 200
        assert "orders" in re.json()
