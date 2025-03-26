import datetime

def read_products(file_path):
    """Зчитує дані про товари з файлу."""
    products = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            name, date_str, price_str = line.strip().split(", ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            price = float(price_str)
            products.append((name, date, price))
    return products


def get_price_change(products, product_name):
    """Визначає зміну ціни на вказаний товар за останній місяць."""
    today = datetime.date.today()
    one_month_ago = today - datetime.timedelta(days=30)

    filtered = [p for p in products if p[0] == product_name and p[1] >= one_month_ago]

    if len(filtered) < 2:
        return f"Недостатньо даних про {product_name}."

    filtered.sort(key=lambda x: x[1])  # Сортуємо за датою

    old_price = filtered[0][2]
    new_price = filtered[-1][2]
    change = new_price - old_price

    return f"Ціна на {product_name} змінилася на {change:.2f} грн."


if __name__ == "__main__":
    file_path = "../products.txt"
    products = read_products(file_path)
    product_name = input("Введіть назву товару: ")
    result = get_price_change(products, product_name)
    print(result)