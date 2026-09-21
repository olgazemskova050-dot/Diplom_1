import pytest

from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun."""

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("", 0),
            ("sesame bun", 150.5),
        ],
    )
    def test_bun_creation_and_getters(self, name, price):
        """Проверка создания булочки и работы геттеров."""
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price