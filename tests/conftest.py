import pytest
from unittest.mock import Mock


@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = 'Краторная булка'
    mock_bun.price = 100
    return mock_bun

@pytest.fixture
def ingredient_mock():
    mock_ingredient = Mock()
    mock_ingredient.name = 'Грибной соус'
    mock_ingredient.price = 50
    mock_ingredient.ingredient_type = 'Соус'
    return mock_ingredient
