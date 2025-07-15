from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == 'Краторная булка'

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[0].name == 'Грибной соус'

    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        ingredient_mock.name = 'Мясо'
        burger.add_ingredient(ingredient_mock)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].name == 'Мясо'

    def test_get_price(self, bun_mock, ingredient_mock):

        bun_mock.get_price.return_value = 150
        ingredient_mock.get_price.return_value = 50

        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == 350

    def test_get_receipt(self, bun_mock, ingredient_mock):
    #обозначаем значения рез-тов методов из классов Bun и Ingredient
        bun_mock.get_name.return_value = 'Флюресцентная булка'
        ingredient_mock.get_name.return_value = 'Соус из моллюсков'
        ingredient_mock.get_type.return_value = 'Соус'
        bun_mock.get_price.return_value = 201
        ingredient_mock.get_price.return_value = 99
    #создаем объект класса Бургер
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
    #формируем чек и из строки вытаскиваем последние 3 символа цены
        check = burger.get_receipt()
        assert check[-3:] == '501'


