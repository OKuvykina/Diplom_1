from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('Космик', 100)
        actual_result = bun.get_name()
        assert actual_result == 'Космик'

    def test_get_price(self):
        bun = Bun('Космик', 100)
        actual_result = bun.get_price()
        assert actual_result == 100