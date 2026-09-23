import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database."""

    @pytest.fixture
    def database(self):
        """Фикстура: база данных с предзаполненными данными."""
        return Database()

    def test_available_buns_returns_three_items(self, database):
        """В базе ровно 3 булочки."""
        assert len(database.available_buns()) == 3

    def test_available_buns_returns_bun_instances(self, database):
        """Все элементы списка булочек — экземпляры Bun."""
        for bun in database.available_buns():
            assert isinstance(bun, Bun)

    def test_available_buns_returns_internal_list(self, database):
        """Метод возвращает тот же объект списка."""
        assert database.available_buns() is database.buns

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
    )
    def test_available_buns_data(self, database, index, expected_name, expected_price):
        """Проверка имени и цены каждой булочки."""
        bun = database.available_buns()[index]
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_available_ingredients_returns_six_items(self, database):
        """В базе ровно 6 ингредиентов."""
        assert len(database.available_ingredients()) == 6

    def test_available_ingredients_returns_ingredient_instances(self, database):
        """Все элементы списка — экземпляры Ingredient."""
        for ingredient in database.available_ingredients():
            assert isinstance(ingredient, Ingredient)

    def test_available_ingredients_returns_internal_list(self, database):
        """Метод возвращает тот же объект списка."""
        assert database.available_ingredients() is database.ingredients

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
    )
    def test_available_ingredients_data(
        self, database, index, expected_type, expected_name, expected_price
    ):
        """Проверка типа, имени и цены каждого ингредиента."""
        ingredient = database.available_ingredients()[index]
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price