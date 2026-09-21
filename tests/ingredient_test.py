import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient."""

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
            (INGREDIENT_TYPE_FILLING, "cutlet", 300),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 400.5),
            (INGREDIENT_TYPE_SAUCE, "", 0),
            ("unknown", "mystery", 999),
        ],
    )
    def test_ingredient_creation_and_getters(self, ingredient_type, name, price):
        """Проверка создания ингредиента и работы всех геттеров."""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price