from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredientTypes:
    """Тесты для констант типов ингредиентов."""

    def test_sauce_type_value(self):
        """Константа соуса имеет ожидаемое значение."""
        assert INGREDIENT_TYPE_SAUCE == "SAUCE"

    def test_filling_type_value(self):
        """Константа начинки имеет ожидаемое значение."""
        assert INGREDIENT_TYPE_FILLING == "FILLING"