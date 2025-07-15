from praktikum.database import Database


class TestBurger:

    def test_available_buns(self):
        database = Database()
        database.available_buns()
        assert database.buns[2].price == 300

    def test_available_ingredients(self):
        database = Database()
        database.available_ingredients()
        assert database.ingredients[-1].price == 300