import allure
import requests
from test_data import *

class TestOrderList:
    @allure.title('Проверить, что в тело ответа возвращается список заказов.')
    def test_get_order_list(self):
        re = requests.get(ORDER_CREATION_AND_LIST_URL)

        assert re.status_code == 200
        assert "orders" in re.json()
