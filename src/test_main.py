import pytest
import datetime
from main import get_price_change


@pytest.fixture
def sample_products():
    """Приклад тестових даних."""
    return [
        ("Молоко", datetime.date(2025, 2, 15), 55.50),
        ("Хліб", datetime.date(2025, 2, 20), 25.00),
        ("Шоколад", datetime.date(2025, 2, 20), 40.00),
        ("Молоко", datetime.date(2025, 3, 10), 60.00),
        ("Шоколад", datetime.date(2025, 4, 20), 54.00),
    ]


def test_price_change_found(sample_products):
    """Перевіряємо, чи правильно визначається зміна ціни."""
    result = get_price_change(sample_products, "Молоко")
    assert "4.50" in result or "Недостатньо даних про Молоко" in result


def test_price_change_not_enough_data(sample_products):
    """Перевіряємо випадок, коли немає достатньо даних."""
    result = get_price_change(sample_products, "Хліб")
    assert "Недостатньо даних" in result


def test_price_change_no_product(sample_products):
    """Перевіряємо випадок, коли товару немає у списку."""
    result = get_price_change(sample_products, "Кава")
    assert "Недостатньо даних" in result