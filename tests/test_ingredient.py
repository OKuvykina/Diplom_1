import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Сыр', 200)
        actual_result = ingredient.get_name()
        assert actual_result == 'Сыр'

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Сыр', 250)
        actual_result = ingredient.get_price()
        assert actual_result == 250

    # проверяем тип ингредиента
    @pytest.mark.parametrize('type_ingredient',
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_type(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, 'Сыр', 200)
        actual_result = ingredient.get_type()
        assert actual_result == type_ingredient