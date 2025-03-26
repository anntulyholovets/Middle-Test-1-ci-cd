import datetime


def get_price_change(products, product_name):
    """Обчислює зміну ціни на товар за останній місяць."""
    today = datetime.date.today()
    one_month_ago = today - datetime.timedelta(days=30)

    # Вибираємо записи за останній місяць
    filtered = [p for p in products if p[0] == product_name and p[1] >= one_month_ago]

    if len(filtered) < 2:
        return f"Недостатньо даних про {product_name}."

    # Сортуємо за датою
    filtered.sort(key=lambda x: x[1])

    old_price = filtered[0][2]
    new_price = filtered[-1][2]
    change = new_price - old_price

    return f"Зміна ціни на {product_name}: {change:.2f} грн."


def read_products(file_path):
    pass


if __name__ == "__main__":
    file_path = "../products.txt"
    products = read_products(file_path)
    product_name = input("Введіть назву товару: ")
    result = get