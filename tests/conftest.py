import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    """Фикстура: новый бургер перед каждым тестом."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура: мок булочки."""
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    """Фикстура: фабрика моков ингредиентов."""
    def _make(name="cutlet", price=200.0, ing_type="FILLING"):
        ing = Mock()
        ing.get_name.return_value = name
        ing.get_price.return_value = price
        ing.get_type.return_value = ing_type
        return ing
    return _make